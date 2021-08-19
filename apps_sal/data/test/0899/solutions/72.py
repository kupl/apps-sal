(n, m) = map(int, input().split())
rg = [[999999999 for _ in range(n)] for _ in range(n)]
rgflg = [[False for _ in range(n)] for _ in range(n)]
for i in range(m):
    (a, b, c) = map(int, input().split())
    rg[a - 1][b - 1] = c
    rgflg[a - 1][b - 1] = True
    rg[b - 1][a - 1] = c
    rgflg[b - 1][a - 1] = True
count = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if rg[i][j] > rg[i][k] + rg[k][j]:
                rg[i][j] = rg[i][k] + rg[k][j]
                if rgflg[i][j] == True or rgflg[j][i] == True:
                    rgflg[i][j] = False
                    rgflg[j][i] = False
                    count += 1
print(count)
