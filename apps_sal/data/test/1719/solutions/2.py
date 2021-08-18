n = int(input())
mod = 10**9 + 7

dp = [[0] * 4 for i in range(n)]
for i in range(4):
    dp[0][i] = 1
    dp[1][i] = 4
    dp[2][i] = 16

dp[2][1] -= 2
dp[2][2] -= 1

for i in range(3, n):
    for j in range(4):
        dp[i][j] = sum(dp[i - 1]) % mod
    dp[i][1] -= dp[i - 2][0]
    dp[i][1] -= dp[i - 2][2]
    dp[i][1] -= dp[i - 3][0] * 3
    dp[i][2] -= dp[i - 2][0]
    dp[i][2] += dp[i - 3][2]

print(sum(dp[n - 1]) % mod)
