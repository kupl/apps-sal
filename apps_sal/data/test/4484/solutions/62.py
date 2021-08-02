def solve():
    N, M = map(int, input().split())
    if abs(N - M) > 1:
        return 0
    mod = 10**9 + 7
    ans = 2 - abs(N - M)
    for i in range(N):
        ans *= i + 1
        ans %= mod
    for i in range(M):
        ans *= i + 1
        ans %= mod
    return ans


print(solve())
