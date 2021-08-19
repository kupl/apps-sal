n = int(input())
dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(n + 1)]
for i in range(4):
    for j in range(4):
        for k in range(4):
            if i == 0 and j == 1 and (k == 2) or (i == 0 and j == 2 and (k == 1)) or (i == 2 and j == 0 and (k == 1)):
                pass
            else:
                dp[3][i][j][k] = 1
for a in range(3, n):
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if j == 0 and k == 1:
                        if l == 2:
                            continue
                    if j == 0 and k == 2:
                        if l == 1:
                            continue
                    if j == 2 and k == 0:
                        if l == 1:
                            continue
                    if i == 0 and k == 2:
                        if l == 1:
                            continue
                    if i == 0 and j == 2:
                        if l == 1:
                            continue
                    dp[a + 1][j][k][l] += dp[a][i][j][k]
                    dp[a + 1][j][k][l] %= 10 ** 9 + 7
ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans += dp[n][i][j][k]
            ans %= 10 ** 9 + 7
print(ans)
