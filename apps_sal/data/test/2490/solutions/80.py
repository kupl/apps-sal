n = [int(x) for x in input()]

dp = [[100000000000 for i in range(len(n) + 1)]for j in range(2)]
dp[0][0] = 0
dp[1][0] = 1
for i in range(len(n)):
    d = n[i]
    dp[0][i + 1] = min(dp[0][i + 1], min(d, 11 - d) + dp[0][i], 10 - d + dp[1][i])
    dp[1][i + 1] = min(dp[1][i + 1], d + 1 + dp[0][i], 9 - d + dp[1][i])


print((dp[0][len(n)]))
