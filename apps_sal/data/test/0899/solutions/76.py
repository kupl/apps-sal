n,m = map(int,input().split())
INF = 10**18
d = [[INF]*n for _ in range(n)]
nd = [[INF]*n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
    nd[i][i] = 0
for _ in range(m):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    d[a][b] = c
    d[b][a] = c
    nd[a][b] = c
    nd[b][a] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            nd[i][j] = min(nd[i][j], nd[i][k]+nd[k][j])

cnt = 0
for i in range(n):
    for j in range(n):
        if d[i][j] == INF: continue
        if nd[i][j] < d[i][j]: cnt += 1
print(cnt//2)
