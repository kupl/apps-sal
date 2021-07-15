from collections import deque

N, M = list(map(int, input().split()))

G = [[] for _ in range(N)]
for i in range(M):
  L, R, D = list(map(int, input().split()))
  G[L-1].append((R-1, D))
  G[R-1].append((L-1, -D))
  
visited = [False] * N
xs = [0] * N
xs[0] = 0
x = 0
for i in range(N):
  if visited[i]:
    continue
  stack = deque([(i, x)])
  visited[i] = True
  while stack:
    now, xi = stack.popleft()
    for nx, di in G[now]:
      if visited[nx]:
        if xs[nx] != xi + di:
          print('No')
          return
      else:
        xs[nx] = xi + di
        visited[nx] = True
        stack.append((nx, xi+di))
        
if max(xs)-min(xs) > 1000000000:
  print('No')
else:
  print('Yes')


