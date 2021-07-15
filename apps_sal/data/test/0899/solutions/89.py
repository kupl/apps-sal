N, M = list(map(int, input().split()))
conns = [tuple(map(int, input().split())) for _ in range(M)]
cost = [[float("INF")]*N for _ in range(N)]

# make same node cost zeros
for i in range(N):
  cost[i][i] = 0

# update edge cost
for a,b,c in conns:
  cost[a-1][b-1] = c
  cost[b-1][a-1] = c

# find minimum cost across all pairs of nodes
for k in range(N):
  for i in range(N):
    for j in range(N):
      cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

# find edges without shortest path
cnt = 0
for a,b,c in conns:
  if c > cost[a-1][b-1]:
    cnt += 1

print(cnt)
  

