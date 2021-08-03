INF = 100000000
N, M = map(int, input().split())
a = [0] * 1000
b = [0] * 1000
c = [0] * 1000
dist = [[INF for _ in range(100)] for _ in range(100)]
for i in range(M):
    a[i], b[i], c[i] = map(int, input().split())
    a[i] -= 1
    b[i] -= 1
for i in range(N):
    for j in range(N):
        if i == j:
            dist[i][j] = 0
for i in range(M):
    dist[a[i]][b[i]] = min(dist[a[i]][b[i]], c[i])
    dist[b[i]][a[i]] = min(dist[b[i]][a[i]], c[i])
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
ans = M
for i in range(M):
    flag = False
    for j in range(N):
        if dist[j][a[i]] + c[i] == dist[j][b[i]]:
            flag = True
    if flag:
        ans -= 1
print(ans)
