def solve(n, k):
    if n == 1:
        return 1
    if k == 2 ** (n - 1):
        return n
    return solve(n - 1, k % (2 ** (n - 1)))


n, k = map(int, input().split())
print(solve(n, k))
