# 292B

__author__ = 'artyom'

read = lambda: map(int, input().split())
n, m = read()
graph = [set() for _ in range(1 + n)]
degrees = [0] * (n + 1)
for __ in range(m):
  u, v = read()
  graph[u].add(v)
  graph[v].add(u)
  degrees[u] += 1
  degrees[v] += 1


def dfs(start):
  stack = [(start, None)]
  visited = [0] * (n + 1)
  while stack:
    v, parent = stack.pop()
    if degrees[v] > 2:
      return 'star' if all([degrees[u] == 1 for u in graph[v]]) else 'unknown'
    for u in graph[v]:
      if u != parent:
        if visited[u]:
          return 'ring' if u == start else 'unknown'
        stack.append((u, v))
    visited[v] = 1
  return 'bus'


print(dfs(1) + ' topology')
