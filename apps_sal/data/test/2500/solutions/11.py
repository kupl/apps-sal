MOD = 10**9 + 7
n = int(input())
s = bin(n)[2:]
dp = [[0, 0, 0] for _ in range(len(s) + 1)]
dp[0][0] = 1
for i in range(len(s)):
    if s[i] == '0':
        dp[i + 1][0] = dp[i][0] + dp[i][1]
        dp[i + 1][1] = dp[i][1]
        dp[i + 1][2] = dp[i][1] + dp[i][2] * 3
    else:
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = dp[i][0] + dp[i][1]
        dp[i + 1][2] = dp[i][1] * 2 + dp[i][2] * 3
    for j in range(3):
        dp[i + 1][j] %= MOD
print((sum(dp[-1]) % MOD))
