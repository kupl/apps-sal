# 445B

__author__ = 'artyom'

read = lambda: map(int, input().split())
n, m = read()
graph = [set() for _ in range(n + 1)]
for __ in range(m):
  x, y = read()
  graph[x].add(y)
  graph[y].add(x)

visited = set()


def dfs(start, counter):
  stack = [start]
  while stack:
    vertex = stack.pop()
    if vertex not in visited:
      counter *= 2
      visited.add(vertex)
      stack.extend(graph[vertex] - visited)
  return counter // 2


res = 1
for v in range(1, n + 1):
  if v not in visited:
    res = dfs(v, res)

print(res)
