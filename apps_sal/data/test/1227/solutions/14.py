N = input()
K = int(input())
m = len(N)
dp = [[[0] * (K + 1) for _ in range(2)] for _ in range(m + 1)]
dp[0][0][0] = 1
for i in range(1, m + 1):
    l = int(N[i - 1])
    for k in range(K + 1):
        if k == 0:
            dp[i][0][k] = 0
            dp[i][1][k] = 1
        elif l != 0:
            dp[i][0][k] = dp[i - 1][0][k - 1]
            dp[i][1][k] = dp[i - 1][1][k] + 9 * dp[i - 1][1][k - 1] + dp[i - 1][0][k] + (l - 1) * dp[i - 1][0][k - 1]
        else:
            dp[i][0][k] = dp[i - 1][0][k]
            dp[i][1][k] = dp[i - 1][1][k] + 9 * dp[i - 1][1][k - 1]
print(dp[m][0][K] + dp[m][1][K])
