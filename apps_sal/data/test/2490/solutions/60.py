N = [int(_) for _ in input()]
dp = [[0, 0] for _ in range(len(N))]
dp[0][0] = min(N[0], 11 - N[0])
dp[0][1] = min(N[0] + 1, 10 - N[0])
for i in range(1, len(N)):
    dp[i][0] = min(dp[i - 1][0] + N[i], dp[i - 1][1] + 10 - N[i])
    dp[i][1] = min(dp[i - 1][0] + N[i] + 1, dp[i - 1][1] + 9 - N[i])
print(dp[-1][0])
