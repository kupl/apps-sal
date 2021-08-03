s = str(input())
n = len(s)
dp = [[0] * 2 for _ in range(n + 1)]
dp[0][1] = 1
for i in range(n):
    p = int(s[i])
    dp[i + 1][0] = min(dp[i][1] + 10 - p, dp[i][0] + p)
    dp[i + 1][1] = min(dp[i][1] + 10 - p - 1, dp[i][0] + p + 1)
print(dp[-1][0])
