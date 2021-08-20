n = int(input())
dp = [float('inf')] * (n + 1)
for i in range(n + 1):
    dp[i] = min(dp[i], i)
    j = 6
    while i + j <= n:
        dp[i + j] = min(dp[i + j], dp[i] + 1)
        j *= 6
    k = 9
    while i + k <= n:
        dp[i + k] = min(dp[i + k], dp[i] + 1)
        k *= 9
print(dp[n])
