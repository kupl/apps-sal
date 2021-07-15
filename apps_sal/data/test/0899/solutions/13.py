N,M = list(map(int,input().split()))

INF = 10**7
dist = [[INF for j in range(N)] for i in range(N)]
d = [[INF for j in range(N)] for i in range(N)]
prev = [[i for j in range(N)] for i in range(N)]
t = [[0 for j in range(N)] for i in range(N)]

# 初期化
for i in range(N):
    d[i][i] = 0
    dist[i][i] = 0

for _ in range(M):
    a,b,c = list(map(int,input().split()))
    dist[a-1][b-1] = c
    dist[b-1][a-1] = c
    d[a-1][b-1] = c
    d[b-1][a-1] = c

#　d[a][b]:aとbの距離
def warshall_floyd(n):
    for k in range(n):
        for i in range(n):#始点
            for j in range(n):#終点
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])

warshall_floyd(N)
ans = 0
for i in range(N):
    for j in range(N):
        if dist[i][j] != INF and d[i][j] != dist[i][j]:
            ans += 1
print((ans//2))

