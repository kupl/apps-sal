n = int(input())
mod = 1000000007
dp = [[[0] * 4 for _ in range(4)] for _ in range(n + 1)]
for j in range(4):
    for k in range(4):
        dp[2][j][k] = 1

for i in range(2, n):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if (j, k, l) in ((2, 1, 0), (1, 2, 0), (1, 0, 2)):
                    continue
                dp[i + 1][j][k] += dp[i][k][l]
                dp[i + 1][j][k] %= mod
    dp[i + 1][1][2] -= dp[i - 1][2][0]
    dp[i + 1][1][2] %= mod
    dp[i + 1][1][3] -= dp[i - 1][2][0]
    dp[i + 1][1][3] %= mod
    dp[i + 1][1][2] -= dp[i - 1][3][0]
    dp[i + 1][1][2] %= mod

ans = 0
for j in range(4):
    for k in range(4):
        ans += dp[n][j][k]
        ans %= mod
print(ans)
