MOD = pow(10, 9) + 7
N = int(input())
dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
dp[0][3][3][3] = 1

for i in range(N):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if dp[i][j][k][l] == 0:
                    continue
                for a in range(4):
                    if a == 2 and j == 1 and k == 0:
                        continue
                    if a == 1 and j == 2 and k == 0:
                        continue
                    if a == 2 and j == 0 and k == 1:
                        continue
                    if a == 2 and j == 1 and l == 0:
                        continue
                    if a == 2 and k == 1 and l == 0:
                        continue
                    dp[i + 1][a][j][k] += dp[i][j][k][l] % MOD
ans = 0
for j in range(4):
    for k in range(4):
        for l in range(4):
            ans += dp[N][j][k][l]
ans = ans % MOD
print(ans)
