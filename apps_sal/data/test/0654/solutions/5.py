n = int(input())
dp = [[[0] * (n + 1) for i in range(n + 1)] for j in range(2)]
dp[0][0][0] = 0
dp[1][0][0] = 0
mod = 10 ** 9 + 7
for i in range(n + 1):
    for j in range(i, n + 1):
        if i == 0 and j == 0:
            continue
        dp[0][i][j] = (dp[1][i - 1][j] + dp[1][i][j - 1]) % mod
        tmp1 = 1
        if i - 1 <= j and i > 0:
            if i <= j - 1:
                tmp1 += dp[1][i][j - 1]
                tmp1 %= mod
            tmp1 += dp[0][i - 1][j]
        tmp1 %= mod
        tmp2 = 1
        if i <= j - 1 and j > 0:
            if i - 1 <= j:
                tmp2 += dp[1][i - 1][j]
                tmp2 %= mod
            tmp2 += dp[0][i][j - 1]
        tmp2 %= mod
        dp[1][i][j] = max(tmp1, tmp2) % mod
print(max(dp[0][-1][-1], dp[1][-1][-1]) % mod)
