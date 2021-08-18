
pri = 998244353
dp = [[[0 for i in range(2001)] for i in range(1001)] for i in range(2)]
n, k = list(map(int, input().split()))
for i in range(1, n + 1):
    if(i == 1):
        dp[0][i][1] = 2
        dp[1][i][2] = 2

        continue
    for j in range(1, (2 * i) + 1):
        dp[0][i][j] = (dp[0][i - 1][j]) + (dp[0][i - 1][j - 1]) + (2 * (dp[1][i - 1][j]))

        dp[0][i][j] %= pri
        dp[1][i][j] = (2 * dp[0][i - 1][j - 1]) + (dp[1][i - 1][j]) + (dp[1][i - 1][j - 2])
        dp[0][i][j] %= pri
        dp[1][i][j] %= pri
y = dp[0][n][k] + dp[1][n][k]
y %= pri
print(y)
