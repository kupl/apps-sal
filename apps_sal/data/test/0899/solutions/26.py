from heapq import heappush, heappop

N, M = map(int, input().split())
INF = 10**10
edge_idx = {}
graph = [[] for i in range(N)]
for i in range(M):
  a, b, c = map(int, input().split())
  a -= 1; b -= 1
  graph[a].append((b, c))
  graph[b].append((a, c))
  edge_idx[(a, b)] = edge_idx[(b, a)] = i

used = set()
def dijkstra(node):
  nonlocal used
  dist = [INF] * N
  dist[node] = 0
  e = []
  for child, cost in graph[node]:
    heappush(e, (cost, child, node))
  while e:
    cost, node, par = heappop(e)
    if dist[node] < INF:
      if dist[node] == cost:
        used.add(edge_idx[(node, par)])
      continue
    dist[node] = cost
    used.add(edge_idx[(node, par)])
    for child, c in graph[node]:
      if dist[child] < INF:
        continue
      heappush(e, (cost+c, child, node))

for i in range(N):
  dijkstra(i)

print(M - len(used))
