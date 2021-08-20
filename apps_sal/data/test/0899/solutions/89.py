(N, M) = list(map(int, input().split()))
conns = [tuple(map(int, input().split())) for _ in range(M)]
cost = [[float('INF')] * N for _ in range(N)]
for i in range(N):
    cost[i][i] = 0
for (a, b, c) in conns:
    cost[a - 1][b - 1] = c
    cost[b - 1][a - 1] = c
for k in range(N):
    for i in range(N):
        for j in range(N):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
cnt = 0
for (a, b, c) in conns:
    if c > cost[a - 1][b - 1]:
        cnt += 1
print(cnt)
