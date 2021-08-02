n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [[0 for i in range(n)] for j in range(2)]
dp[0][0] = a[0]
for i in range(1, n):
    dp[0][i] = a[i] + dp[0][i - 1]
dp[1][0] = dp[0][0] + b[0]
for i in range(1, n):
    dp[1][i] = max(dp[0][i], dp[1][i - 1]) + b[i]
print((dp[1][n - 1]))
