def main():
    MOD = 10 ** 9 + 7

    s = input()
    n = len(s)

    dp = [[0] * 4 for _ in range(n + 1)]
    dp[0][0] = 1

    for i, c in enumerate(s, start=1):
        for j in range(4):
            dp[i][j] = dp[i - 1][j]
        if c == 'A':
            dp[i][1] += dp[i - 1][0]
        elif c == 'B':
            dp[i][2] += dp[i - 1][1]
        elif c == 'C':
            dp[i][3] += dp[i - 1][2]
        else:
            for j in range(1, 4):
                dp[i][j] += dp[i - 1][j - 1]
            for j in range(4):
                dp[i][j] += dp[i - 1][j] * 2
        for j in range(4):
            dp[i][j] %= MOD

    print((dp[n][3]))


def __starting_point():
    main()

__starting_point()
