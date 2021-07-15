
def resolve():
    S = input()
    n = len(S)
    dp = [[0] * 2 for _ in range(n + 1)]
    dp[0][1] = 1
    for i in range(1, n + 1):
        d = int(S[i - 1])
        dp[i][0] = min(dp[i - 1][0] + d, dp[i - 1][1] + (10 - d))
        dp[i][1] = min(dp[i - 1][0] + (d + 1), dp[i - 1][1] + (10 - 1 - d))
    print((dp[n][0]))


def __starting_point():
    resolve()

__starting_point()
