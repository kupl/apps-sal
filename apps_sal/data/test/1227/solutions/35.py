n = input()
K = int(input())
len_n = len(n)
dp = [[[0] * 2 for _ in range(K + 2)] for _ in range(len_n + 1)]


dp[0][0][1] = 1
for i in range(1, len_n + 1):
    d = int(n[i - 1])
    for j in range(K + 1):
        dp[i][j][0] += dp[i - 1][j][0]
        dp[i][j + 1][0] += dp[i - 1][j][0] * 9
        if 0 < d:
            dp[i][j + 1][0] += dp[i - 1][j][1] * (d - 1)
            dp[i][j][0] += dp[i - 1][j][1]
            dp[i][j + 1][1] += dp[i - 1][j][1]
        else:
            dp[i][j][1] += dp[i - 1][j][1]

ans = dp[-1][K][0] + dp[-1][K][1]
print(ans)
