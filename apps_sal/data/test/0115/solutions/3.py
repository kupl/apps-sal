r, s, p = [int(x) for x in input().split()]
dp = [[[0 for i in range(105)] for j in range(105)] for k in range(105)]

dp[r][s][p] = 1

for i in range(r, -1, -1):
    for j in range(s, -1, -1):
        for k in range(p, -1, -1):

            dnr = i * j + j * k + i * k

            if i > 0 and j > 0:
                dp[i][j - 1][k] += (i * j * dp[i][j][k]) / dnr
            if j > 0 and k > 0:
                dp[i][j][k - 1] += (j * k * dp[i][j][k]) / dnr
            if k > 0 and i > 0:
                dp[i - 1][j][k] += (k * i * dp[i][j][k]) / dnr

roc, sci, pap = [0] * 3

for i in range(105):
    roc += dp[i][0][0]
    sci += dp[0][i][0]
    pap += dp[0][0][i]


print(roc, sci, pap)
