from scipy.sparse.csgraph import floyd_warshall
import itertools

N, M, R = map(int, input().split())
r = list(map(int, input().split()))
r = [ri-1 for ri in r]

graph = [[0]*N for i in range(N)]
for i in range(M):
  a, b, c = map(int, input().split())
  a -= 1; b -= 1
  graph[a][b] = graph[b][a] = c

dist = floyd_warshall(graph).astype(int)
orders = list(itertools.permutations(r, R))

ans = float('inf')
for order in orders:
  d = 0
  for u, v in zip(order, order[1:]):
    d += dist[u][v]
  ans = min(ans, d)

print(ans)
