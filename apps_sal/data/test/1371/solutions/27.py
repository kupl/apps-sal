def calculate(n):
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    MOD = 1000000000 + 7
    for i in range(1, n+1):
        x = 0
        for j in range(i - 3 + 1):
            x += (dp[j] % MOD)
        dp[i] = x

    print((dp[n] % MOD))


calculate(int(input()))

