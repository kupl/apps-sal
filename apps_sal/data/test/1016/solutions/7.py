n, m = map(int, input().split())

g = [[False] * n for i in range(n)]

for i in range(m):
  x, y = map(int, input().split())
  x -= 1
  y -= 1
  g[x][y] = g[y][x] = True

u = [False] * n
d = 1

def dfs(p):
  nonlocal d
  for j in range(n):
    if g[p][j] and not u[j]:
      u[j] = True
      d *= 2
      dfs(j)

for i in range(n):
  if not u[i]:
    u[i] = True
    dfs(i)

print(d)
