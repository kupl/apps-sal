L = list(input())
dp = [[0 for _ in range(2)] for _ in range(100005)]
MOD = 10 ** 9 + 7
dp[0][0] = 1
for (i, l) in enumerate(L, 1):
    if l == '1':
        dp[i][0] = dp[i - 1][0] * 2 % MOD
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][1] * 3) % MOD
    else:
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 1][1] * 3 % MOD
print((dp[i][0] + dp[i][1]) % MOD)
