n = int(input())
dp = [[0 for i in range(3)] for j in range(n + 1)]
a = list(map(int, input().split()))
for i in range(1, n + 1):
    if a[i - 1] == 1 or a[i - 1] == 3:
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + 1
    if a[i - 1] == 2 or a[i - 1] == 3:
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + 1
    dp[i][0] = max(max(dp[i - 1][0], dp[i - 1][1]), dp[i - 1][2])

print(n - max(max(dp[n][0], dp[n][1]), dp[n][2]))
