import sys
readline = sys.stdin.readline

N = int(readline())

G = [[] for i in range(N)]
from collections import defaultdict
E = defaultdict(int)

for i in range(N - 1):
  a,b = map(int,readline().split())
  G[a - 1].append(b - 1)
  G[b - 1].append(a - 1)
  E[(a - 1, b - 1)] = i

from collections import deque
q = deque([])
ans = [None] * (N - 1)

q.append([0, -1, 0])
maxcol = 0
while q:
  v, parent, color = q.popleft()
  if color > maxcol:
    maxcol = color
  if (v, parent) in E:
    ans[E[(v, parent)]] = color
  elif (parent, v) in E:
    ans[E[(parent, v)]] = color
  next_col = 0
  for child in G[v]:
    if child == parent:
      continue
    next_col += 1
    if next_col == color:
      next_col += 1
    q.append([child, v, next_col])
    
print(maxcol)
for a in ans:
  print(a)
