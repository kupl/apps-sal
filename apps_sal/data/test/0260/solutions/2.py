def dfs(n, k, cache={}):
    if k > n or k < 0:
        return 0
    if k == 0 or k == n:
        return 1
    if (n, k) in cache:
        return cache[n, k]
    z = cache[n, k] = dfs(n - 1, k - 1) + dfs(n - 1, k)
    return z


def bits(n):
    b = 0
    while n:
        if n & 1:
            b += 1
        n >>= 1
    return b


def count(n, k):
    (z, b, c) = (0, 63, 0)
    for b in reversed(range(64)):
        if n >> b & 1:
            z += dfs(b, k - c)
            c += 1
        if not k:
            break
    return z + (bits(n) == k)


def solve(m, k):
    (low, high) = (1, 10 ** 18)
    while low < high:
        mid = (low + high) // 2
        if count(2 * mid, k) - count(mid, k) < m:
            low = mid + 1
        else:
            high = mid
    return high


(m, k) = [int(x) for x in input().split()]
print(solve(m, k))
