(c, d) = map(int, input().split())
(n, m) = map(int, input().split())
k = int(input())
dp = [0] * ((n + 1) * m + k)
for i in range(1, n * m - k + 1):
    dp[i] = min(dp[i - 1] + d, dp[i - n] + c)
print(dp[n * m - k])
