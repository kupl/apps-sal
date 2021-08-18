n, x = list(map(int, input().split()))
a = list(map(int, input().split()))
dp = [[0 for i in range(3)] for j in range(n + 1)]
a = [0] + a
res = 0
for i in range(1, n + 1):
    dp[i][0] = max(0, dp[i - 1][0] + a[i], a[i])
    dp[i][1] = max(0, dp[i - 1][0] + a[i] * x, dp[i - 1][1] + a[i] * x, a[i] * x)
    dp[i][2] = max(0, a[i], dp[i - 1][0] + a[i], dp[i - 1][1] + a[i], dp[i - 1][2] + a[i])
    res = max(res, dp[i][0], dp[i][1], dp[i][2])
print(res)
