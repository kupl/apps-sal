n = int(input())
INF = float('inf')
dp = [INF] * 100010
dp[0] = 0
pow6 = [6 ** i for i in range(1, 7)]
pow9 = [9 ** i for i in range(1, 6)]
for i in range(1, n + 1):
    dp[i] = dp[i - 1] + 1
    for p6 in pow6:
        dp[i] = min(dp[i], dp[i - p6] + 1)
    for p9 in pow9:
        dp[i] = min(dp[i], dp[i - p9] + 1)
print(dp[n])
