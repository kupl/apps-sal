(n, p, q, r) = map(int, input().split())
a = list(map(int, input().split()))
dp = [[0, 0, 0] for i in range(n)]
dp[0][0] = p * a[0]
dp[0][1] = dp[0][0] + q * a[0]
dp[0][2] = dp[0][1] + r * a[0]
for i in range(1, n):
    dp[i][0] = max(dp[i - 1][0], p * a[i])
    dp[i][1] = max(dp[i - 1][1], dp[i][0] + q * a[i])
    dp[i][2] = max(dp[i - 1][2], dp[i][1] + r * a[i])
print(dp[n - 1][2])
