inp = input().split()
n, p, t = int(inp[0]), float(inp[1]), int(inp[2])
dp = [[0] * (n + 2) for i in range(t + 2)]
dp[0][0] = 1.0
for i in range(t + 1):
    for j in range(n + 1):
        if j == n:
            dp[i + 1][j] += dp[i][j]
        else:
            dp[i + 1][j + 1] += dp[i][j] * p
            dp[i + 1][j] += dp[i][j] * (1 - p)
print(sum(dp[t][i] * i for i in range(n + 1)))
