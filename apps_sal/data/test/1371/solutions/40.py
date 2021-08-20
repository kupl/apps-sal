def __starting_point():
    S = int(input())
    MOD = 10 ** 9 + 7
    if S < 3:
        print(0)
        return
    dp = [0] * (S + 1)
    dp[0] = 1
    for s in range(3, S + 1):
        dp[s] = (dp[s - 3] + dp[s - 1]) % MOD
    print(dp[S])


__starting_point()
