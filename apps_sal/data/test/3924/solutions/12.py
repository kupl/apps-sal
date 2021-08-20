def read():
    return list(map(int, input().split()))


def solve(n, k, A):
    (ans, prev) = (0, 0)
    for a in A:
        total = prev + a
        if prev and total < k:
            ans += 1
            total = 0
        elif total >= k:
            ans += total // k
            total %= k
        prev = total
    ans += prev // k
    ans += 1 if prev % k > 0 else 0
    return ans


(n, k) = read()
A = read()
print(solve(n, k, A))
