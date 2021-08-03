def main():
    L = str(input())
    dp = [[0, 0] for _ in range(len(L))]
    dp[0][0] = 1
    dp[0][1] = 2
    MOD = 10**9 + 7
    for i in range(1, len(L)):
        if L[i] == '1':
            dp[i][0] = 3 * dp[i - 1][0] + dp[i - 1][1]
            dp[i][0] %= MOD
            dp[i][1] = 2 * dp[i - 1][1]
            dp[i][1] %= MOD
        else:
            dp[i][0] = 3 * dp[i - 1][0]
            dp[i][0] %= MOD
            dp[i][1] = dp[i - 1][1]
    print((dp[-1][0] + dp[-1][1]) % MOD)


def __starting_point():
    main()


__starting_point()
