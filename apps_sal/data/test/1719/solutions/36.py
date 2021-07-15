n = int(input())
#dp[i][x][y][z] i文字目、3つ前がx, 2つ前がy, 1つ前がz
#A->0, C->1, G->2, T->3
#だめなパターンはA-GC, AG-C, GAC, ACGのみ

dp = [[[[0]*4 for i in range(4)] for j in range(4)] for k in range(n+1)]
for i in range(4):
    for j in range(4):
        for k in range(4):
            dp[3][i][j][k] = 1
dp[3][0][2][1] = 0
dp[3][0][1][2] = 0
dp[3][2][0][1] = 0

for i in range(3, n):
    for x in range(4):
        for y in range(4):
            for z in range(4):
                for w in range(4):
                    if (y, z, w) == (2, 0, 1):
                        continue
                    if (y, z, w) == (0, 1, 2):
                        continue
                    if (y, z, w) == (0, 2, 1):
                        continue
                    if (x, y, w) == (0, 2, 1):
                        continue
                    if (x, z, w) == (0, 2, 1):
                        continue
                    dp[i+1][y][z][w] += dp[i][x][y][z]
                    dp[i+1][y][z][w] %= 10**9+7
ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans += dp[n][i][j][k]
print((ans%(10**9+7)))

