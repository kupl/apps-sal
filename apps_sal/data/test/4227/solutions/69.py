import sys
readline = sys.stdin.readline

N,M = map(int,readline().split())
G = [[] for i in range(N)]

for i in range(M):
  a,b = map(int,readline().split())
  G[a - 1].append(b - 1)
  G[b - 1].append(a - 1)

stack = []
stack.append([0, set()])
ans = 0
while stack:
  v, visited = stack.pop()
  visited.add(v)
  if len(visited) == N:
    ans += 1
    continue
  for child in G[v]:
    if child in visited:
      continue
    visited_c = visited.copy()
    stack.append([child, visited_c])
  
print(ans)
