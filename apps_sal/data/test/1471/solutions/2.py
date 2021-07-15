N = int(input())
Tree = [[] for _ in range(N+1)]
UVW = []

for _ in range(N-1):
  u, v, w = map(int, input().split())
  Tree[u].append(v)
  Tree[v].append(u)
  UVW.append((u, v, w))

root = 1
parent = [0] * (N+1)
order = []
stack = [root]

while stack:
    x = stack.pop()
    order.append(x)
    for y in Tree[x]:
        if y == parent[x]:
            continue
        parent[y] = x
        stack.append(y)

dis = [0] * (N+1)

for u, v, w in UVW:
  if parent[u] == v:
    dis[u] = w
  else:
    dis[v] = w

color = [-1] * (N+1)
color[root] = 0

for x in order:
  for y in Tree[x]:
    if y == parent[x]:
      continue
    if dis[y]%2 == 0:
      color[y] = color[x]
    else:
      color[y] = color[x] ^ 1

for i in range(1, N+1):
  print(color[i])
