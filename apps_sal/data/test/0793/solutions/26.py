from collections import defaultdict


def solve():
    ans = 0
    mod = 10**9 + 7
    s = defaultdict(lambda: -1)
    t = defaultdict(lambda: -1)
    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for j in range(M + 1):
        dp[0][j] = 1
    for i in range(1, N + 1):
        dp[i][0] = 1
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] += dp[i - 1][j] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
            dp[i][j] %= mod
    ans = dp[-1][-1] % mod
    return ans


print(solve())
