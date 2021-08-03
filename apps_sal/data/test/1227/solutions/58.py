N = input()
n = len(N)
k = int(input())
dp = [[[0] * 2 for _ in range(k + 1)]for _ in range(n + 1)]
dp[0][0][1] = 1
for i in range(1, n + 1):
    d = int(N[i - 1])
    for j in range(k + 1):
        if 0 <= j - 1:
            dp[i][j][0] += dp[i - 1][j - 1][0] * 9
        dp[i][j][0] += dp[i - 1][j][0]
        if d:
            if 0 <= j - 1:
                dp[i][j][1] += dp[i - 1][j - 1][1]
                dp[i][j][0] += dp[i - 1][j - 1][1] * (d - 1)
            dp[i][j][0] += dp[i - 1][j][1]
        else:
            dp[i][j][1] += dp[i - 1][j][1]

ans = dp[-1][-1][0] + dp[-1][-1][1]
print(ans)
