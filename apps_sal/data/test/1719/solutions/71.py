n = int(input())
dp = [[[[1] * 4 for i in range(4)] for j in range(4)] for k in range(n + 1)]
dp[3][1][2][0] = 0
dp[3][1][0][2] = 0
dp[3][2][1][0] = 0
if n > 3:
    for i in range(4, n + 1):
        for j in range(4):
            for k in range(4):
                dp[i][3][j][k] = sum(dp[i - 1][j][k])
                dp[i][0][j][k] = sum(dp[i - 1][j][k])
                if j == 1 and k == 0:
                    dp[i][2][j][k] = 0
                else:
                    dp[i][2][j][k] = sum(dp[i - 1][j][k])
                if j == 0 and k == 2:
                    dp[i][1][j][k] = 0
                elif j == 2 and k == 0:
                    dp[i][1][j][k] = 0
                elif k == 2:
                    dp[i][1][j][2] = sum(dp[i - 1][j][k]) - dp[i - 1][j][2][0]
                elif j == 2:
                    dp[i][1][2][k] = sum(dp[i - 1][j][k]) - dp[i - 1][2][k][0]
                else:
                    dp[i][1][j][k] = sum(dp[i - 1][j][k])
ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans += dp[n][i][j][k] % (10 ** 9 + 7)
print(ans % (10 ** 9 + 7))
