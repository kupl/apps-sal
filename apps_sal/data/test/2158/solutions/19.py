def solve(u, graph, visited):
  visited[u] = True
  current = 0
  for v in graph[u]:
    if not visited[v]:
      current = max(current, solve(v, graph, visited) + graph[u][v])
  return current

def __starting_point():
  N = int(input().strip())
  graph = {x: {} for x in range(N)}
  visited = [False for _ in range(N + 1)]
  for i in range(N - 1):
    u,v,c = list(map(int, input().strip().split(" ")))
    graph[u][v] = c
    graph[v][u] = c
  ans = solve(0, graph, visited)
  print(ans)


__starting_point()
