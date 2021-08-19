(n, m, h) = list(map(int, input().split()))
maks_kol = list(map(int, input().split()))
maks_wie = list(map(int, input().split()))
gora = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(m):
        if gora[i][j] == 1:
            gora[i][j] = min(maks_wie[i], maks_kol[j])
for j in range(n):
    for i in range(m):
        if i < m - 1:
            print(gora[j][i], end=' ')
        else:
            print(gora[j][i], end='\n')
