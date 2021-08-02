n = int(input())
dp = [[0] * 4 for i in range(n + 1)]
mod = 10**9 + 7

dp[0][0] = dp[0][1] = dp[0][2] = dp[0][3] = 1
dp[1][0] = dp[1][1] = dp[1][2] = dp[1][3] = 4

for i in range(2, n):
    for j in range(4):
        dp[i][j] = sum(dp[i - 1]) % mod
    dp[i][1] -= dp[i - 2][0]
    dp[i][2] -= (dp[i - 2][0] + dp[i - 2][1])
    if i >= 3:
        dp[i][2] -= 3 * dp[i - 3][0]
        dp[i][1] += dp[i - 3][1]


print(sum(dp[n - 1]) % mod)
