N, M = map(int, input().split())
INF = 10**10
graph = [[INF for _ in range(N)] for _ in range(N)]

C = []
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c
    C.append([a - 1, b - 1, c])

cnt = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if(i == j):
                graph[i][j] = 0
                continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = M
for u, v, w in C:
    Flg = False
    for i in range(N):
        if(graph[i][v] + w == graph[i][u]):
            Flg = True
    if Flg:
        ans -= 1
print(ans)
