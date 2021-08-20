N = int(input())
MOD = 10 ** 9 + 7
dp = [[[[0 for i in range(4)] for i in range(4)] for i in range(4)] for i in range(N + 1)]
dp[0][0][0][0] = 1
for i in range(1, N + 1):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                for m in range(4):
                    if k == 1 and l == 2 and (m == 3):
                        continue
                    if k == 2 and l == 1 and (m == 3):
                        continue
                    if k == 1 and l == 3 and (m == 2):
                        continue
                    if j == 1 and l == 2 and (m == 3):
                        continue
                    if j == 1 and k == 2 and (m == 3):
                        continue
                    dp[i][k][l][m] += dp[i - 1][j][k][l]
                    dp[i][k][l][m] %= MOD
ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans += dp[N][i][j][k]
            ans %= MOD
print(ans)
