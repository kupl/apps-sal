import numpy as np

s = input()
n = int(s)
k = int(input())

m = len(s)
dp = np.zeros((m + 1, 2, k + 2), dtype=np.int64)
dp[0][1][0] = 1
for cs in range(m):
    cn = int(s[cs])
    for ck in range(k + 2):
        if ck == k + 1:
            nk = ck
        else:
            nk = ck + 1
        dp[cs + 1][0][nk] += 9 * dp[cs][0][ck]
        dp[cs + 1][0][ck] += dp[cs][0][ck]

        if cn == 0:
            dp[cs + 1][1][ck] += dp[cs][1][ck]
        else:
            dp[cs + 1][1][nk] += dp[cs][1][ck]
            dp[cs + 1][0][nk] += (cn - 1) * dp[cs][1][ck]
            dp[cs + 1][0][ck] += dp[cs][1][ck]
print(dp[m][0][k] + dp[m][1][k])
