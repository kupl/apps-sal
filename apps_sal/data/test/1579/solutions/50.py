import sys
sys.setrecursionlimit(1000000)

N = int(input().strip())

X = {}
Y = {}
G = (X, Y)

for _ in range(N):
  x, y = list(map(int, input().strip().split()))
  if x not in X: X[x] = []
  if y not in Y: Y[y] = []
  X[x].append(y)
  Y[y].append(x)


def dfs_visit(visited, u, i):
  if u in visited[i]: return
  visited[i].add(u)
  for v in G[i][u]:
    dfs_visit(visited, v, (i + 1) % 2)


count = 0
i = 0
while len(X) > 0:
  visited = (set(), set())
  x = X.__iter__().__next__()
  dfs_visit(visited, x, 0)

  for x in visited[0]:
    count += len(visited[1]) - len(X.pop(x))

print(count)

