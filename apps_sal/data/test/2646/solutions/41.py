import sys
readline = sys.stdin.readline

N,M = list(map(int,readline().split()))
G = [[] for i in range(N)]
for i in range(M):
  a,b = list(map(int,readline().split()))
  G[a - 1].append(b - 1)
  G[b - 1].append(a - 1)

# 1の部屋からBFSして、初めて来た部屋だったら直前の部屋番号(+1)を入れる
ans = [None] * N

from collections import deque
q = deque([])

q.append((0, -1))
while q:
  v, parent = q.popleft()
  if ans[v] is not None:
    continue
  ans[v] = parent + 1
  for child in G[v]:
    if child == parent:
      continue
    q.append((child, v))

print("Yes")
for i in range(1, len(ans)):
  print((ans[i]))

