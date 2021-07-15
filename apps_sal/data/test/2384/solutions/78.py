n = int(input())
a = [int(i) for i in input().split()]
k = 1 + n%2
dp = [[-float('inf')] * (k + 2) for i in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for j in range(k + 1):
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
        now = dp[i][j]
        if (i + j) % 2 == 0:
            now += a[i]
        dp[i + 1][j] = max(dp[i + 1][j], now)
print(dp[n][k])
