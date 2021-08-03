N = input()[::-1]
l = len(N)
dp = [[0, 0] for i in range(l + 1)]

for i in range(l):
    dp[i + 1][0] = min(dp[i][0] + int(N[i]), dp[i][1] + int(N[i]) + 1)
    if i == 0:
        dp[i + 1][1] = 10 - int(N[i])
    else:
        dp[i + 1][1] = min(dp[i][0] + 10 - int(N[i]), dp[i][1] + 9 - int(N[i]))

print((min(dp[-1][0], dp[-1][1] + 1)))
