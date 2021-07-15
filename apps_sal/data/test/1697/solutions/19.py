# 510B
__author__ = 'artyom'

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(input())


def neighbours(vertex, colour):
  x, y = vertex
  res = []
  if x > 0 and graph[x - 1][y] == colour:
    res.append((x - 1, y))
  if y > 0 and graph[x][y - 1] == colour:
    res.append((x, y - 1))
  if x < n - 1 and graph[x + 1][y] == colour:
    res.append((x + 1, y))
  if y < m - 1 and graph[x][y + 1] == colour:
    res.append((x, y + 1))
  return res


def find_cycle(x, y):
  colour = graph[x][y]
  visited = set()
  stack = [((x, y), None)]
  while stack:
    v, parent = stack.pop()
    if v in visited:
      return set()
    visited.add(v)
    for u in neighbours(v, colour):
      if u != parent:
        stack.append((u, v))
  return visited


visited = set()
for i in range(n):
  for j in range(m):
    if (i, j) not in visited:
      t = find_cycle(i, j)
      if not t:
        print('Yes')
        return
      visited |= t

print('No')
