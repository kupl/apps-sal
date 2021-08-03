n = int(input())
dp = [[0] * (n + 7) for i in range(7)]

for j in range(n + 1):
    dp[0][j] = 1

for i in range(5):
    for j in range(1, n + 1):
        for k in range(5):
            dp[i][j] += dp[i - k][j - 1]

print(dp[2][n] * dp[4][n])
