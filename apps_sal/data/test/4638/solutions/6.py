(n, c) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [[0] * 2 for i in range(n)]
dp[0][1] = c
for i in range(n - 1):
    dp[i + 1][0] = min(dp[i][0] + a[i], dp[i][1] + a[i])
    dp[i + 1][1] = min(dp[i][0] + b[i] + c, dp[i][1] + b[i])
ans = [0] * n
for i in range(n):
    ans[i] = min(dp[i])
print(*ans)
