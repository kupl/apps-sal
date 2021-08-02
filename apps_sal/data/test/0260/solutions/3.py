def dfs(n, k, cache={}):
    # if number of bits is bigger than the number's bits of the number's bits is less than 0
    if k > n or k < 0: return 0
    # if num bits is 0 or num bits is equivalent to the number's bits
    if k == 0 or k == n: return 1
    # This optimization is not necessary but flips the 0s and the 1s
    # if k*2 > n: k = n-k
    # Check is already calculated
    if (n, k) in cache: return cache[(n, k)]
    # Use dfs addition for case where certain bit is 1 or certain bit is 0
    z = cache[(n, k)] = dfs(n - 1, k - 1) + dfs(n - 1, k)
    return z


def bits(n):
    b = 0
    while n:
        if n & 1: b += 1
        n >>= 1
    return b


def count(n, k):
    z, b, c = 0, 63, 0
    for b in reversed(range(64)):
        # Taking n and checking if certain bit is 1 or not
        # This sums for every mod power of 2 that exists to account for every case
        if (n >> b) & 1:
            # calculates by subtracting for bits not accounted for
            z += dfs(b, k - c)
            c += 1
        # if not k: break
    return z + (bits(n) == k)


def solve(m, k):
    # Binary Search for number 1-10^18
    low, high = 1, 10**18
    while low < high:
        mid = (low + high) // 2
        if count(2 * mid, k) - count(mid, k) < m:
            low = mid + 1
        else:
            high = mid
    return high


m, k = [int(x) for x in input().split()]
print(solve(m, k))
