N,M = map(int,input().split())
ABC = [tuple(map(int,input().split())) for i in range(M)]

INF = float('inf')
ds = [[INF]*N for _ in range(N)]
for i in range(N):
    ds[i][i] = 0
for a,b,c in ABC:
    a,b = a-1,b-1
    ds[a][b] = ds[b][a] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            ds[i][j] = min(ds[i][j], ds[i][k] + ds[k][j])

ans = 0
for a,b,c in ABC:
    a,b = a-1,b-1
    if c != ds[a][b]:
        ans += 1
print(ans)
