n, m = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(n):
  print(len(graph[i+1]))
