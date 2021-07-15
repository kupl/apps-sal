# 頂点数がN(N-1)/2, 辺がN(N-2)本できる
from collections import deque

N = int(input())
matches = [[a-1 for a in map(int, input().split())] for line in range(N)]
q = deque(range(N))
depth = [0]*N
waiting = [-1]*N

while q:
  a = q.popleft()
  b = matches[a].pop()
  if waiting[b] == a:
    depth[a] = depth[b] = max(depth[a], depth[b]) + 1
    if matches[a]:
      q.append(a)
    if matches[b]:
      q.append(b)
  else:
    waiting[a] = b
    
if any(matches):
  print(-1)
else:
  print(max(depth))
