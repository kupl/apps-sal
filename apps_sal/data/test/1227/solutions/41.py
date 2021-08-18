n = input()
l = len(n)
k = int(input())
dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(l + 1)]
dp[0][0][0] = 1
for i in range(l):
    nd = int(n[i])
    if nd == 0:
        for j in range(k + 1):
            dp[i + 1][0][j] += dp[i][0][j]
    else:
        for j in range(k + 1):
            dp[i + 1][1][j] += dp[i][0][j]
        for j in range(k):
            dp[i + 1][0][j + 1] += dp[i][0][j]
            dp[i + 1][1][j + 1] += dp[i][0][j] * (nd - 1)
    for j in range(k):
        dp[i + 1][1][j + 1] += dp[i][1][j] * 9
    for j in range(k + 1):
        dp[i + 1][1][j] += dp[i][1][j]
print(dp[l][0][k] + dp[l][1][k])
