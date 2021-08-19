def main():
    S = list(map(int, list(input())))
    N = len(S)
    dp = [[0, 0] for _ in range(N + 1)]
    dp[0][1] = 2
    for i in range(N):
        s = S[i]
        dp[i + 1][0] = min(dp[i][0] + s, dp[i][1] + s)
        dp[i + 1][1] = min(dp[i][0] + 11 - s, dp[i][1] + 9 - s)
    print(min(dp[N][0], dp[N][1]))


def __starting_point():
    main()


__starting_point()
