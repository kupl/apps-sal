import sys
readline = sys.stdin.readline

N = int(readline())
G = [[] for i in range(N)]

for i in range(N - 1):
  u,v,w = map(int,readline().split())
  G[u - 1].append((v - 1, w))
  G[v - 1].append((u - 1, w))
  
color = [-1] * N
stack = []
stack.append([0, -1, 0])
while stack:
  v,parent,cost = stack.pop()
  color[v] = cost
  for child in G[v]:
    if child[0] == parent:
      continue
    stack.append([child[0], v, (cost + child[1]) % 2])

for c in color:
  print(c)
