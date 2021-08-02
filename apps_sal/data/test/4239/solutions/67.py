n = int(input())

dp = [n] * 100010
dp[0] = 0
pow69 = [6**i for i in range(1, 7)] + [9**i for i in range(1, 6)]

for i in range(1, n + 1):
    dp[i] = dp[i - 1] + 1
    for p in pow69:
        dp[i] = min(dp[i], dp[i - p] + 1)

print(dp[n])
