n = input()
k = int(input())

dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(len(n) + 1)]
dp[0][0][0] = 1

for i in range(1, len(n) + 1):
    t = int(n[i - 1])
    for j in range(k + 1):
        if t != 0:
            if j != 0:
                dp[i][0][j] += dp[i - 1][0][j - 1]
                dp[i][1][j] += dp[i - 1][1][j - 1] * 9 + dp[i - 1][0][j - 1] * (t - 1)
            dp[i][1][j] += (dp[i - 1][1][j] + dp[i - 1][0][j])
        else:
            dp[i][0][j] += dp[i - 1][0][j]
            if j != 0:
                dp[i][1][j] += dp[i - 1][1][j - 1] * 9
            dp[i][1][j] += dp[i - 1][1][j]

print(dp[len(n)][0][k] + dp[len(n)][1][k])
