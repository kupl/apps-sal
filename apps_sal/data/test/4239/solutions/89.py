import math
n = int(input())

dp = [math.inf] * (n + 1)

for i in range(n + 1):
    dp[i] = min(dp[i], i)
    j = 6
    while(i + j <= n):
        dp[i + j] = min(dp[i + j], dp[i] + 1)
        j *= 6
    j = 9
    while(i + j <= n):
        dp[i + j] = min(dp[i + j], dp[i] + 1)
        j *= 9
print((dp[n]))
