from collections import deque

n,m = map(int, input().split())

connected = [set() for i in range(n+1)]

for i in range(m):
  a,b = map(int, input().split())
  connected[a].add(b)
  connected[b].add(a)
  
def bfs(x):
  queue = deque([x])
  d = [None] * (n+1)
  d[x] = 0
  while queue:
    v = queue.popleft()
    for i in connected[v]:
      if d[i] is None:
        d[i] = v
        queue.append(i)
  return d

print('Yes')
ans = bfs(1)[2:]

for i in ans:
  print(i)
