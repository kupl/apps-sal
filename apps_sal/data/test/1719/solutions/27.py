MOD = 10 ** 9 + 7
N = int(input())
dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
dp[0][3][3][3] = 1
for len in range(N):
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if dp[len][i][j][k] == 0:
                    continue

                for l in range(4):
                    if l == 2 and i == 1 and j == 0:
                        continue
                    if l == 2 and i == 0 and j == 1:
                        continue
                    if l == 1 and i == 2 and j == 0:
                        continue
                    if l == 2 and i == 1 and k == 0:
                        continue
                    if l == 2 and j == 1 and k == 0:
                        continue
                    dp[len + 1][l][i][j] += dp[len][i][j][k]
                    dp[len + 1][l][i][j] %= MOD
ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans += dp[N][i][j][k]
            ans %= MOD
print(ans)
