n, m = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(m)]

edge = set()
INF = float('inf')
cost = [[INF]*n for _ in range(n)]
for i in range(n):
    cost[i][i] = 0
for a, b, c in abc:
    a, b = a-1, b-1
    cost[a][b] = c
    cost[b][a] = c
    edge.add((a, b, c))

for k in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])

ans = 0
for a, b, c in edge:
    if cost[a][b] < c:
        ans += 1
print(ans)
