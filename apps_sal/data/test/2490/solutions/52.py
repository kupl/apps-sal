
def resolve():
    S = "0" + input()
    N = len(S)

    dp = [[1 << 60] * 2 for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        now = int(S[i])
        dp[i + 1][0] = min(dp[i][0] + now, dp[i][1] + (10 - now))
        dp[i + 1][1] = min(dp[i][0] + now + 1, dp[i][1] + (10 - now - 1))
    print((dp[N][0]))


def __starting_point():
    resolve()


__starting_point()
