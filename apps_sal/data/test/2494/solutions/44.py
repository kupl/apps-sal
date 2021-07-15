import sys
from collections import deque
sys.setrecursionlimit(10**7)
k=int(input())
g=[[] for i in range(k)]
for i in range(k):
  g[i].append(((i+1)%k,1))
  if i:
    g[i].append((10*i%k,0))
dq=deque([1])
res=[float('inf')]*k
res[1]=1
while dq:
  v=dq.popleft()
  if v==0:
    break
  for t,cost in g[v]:
    if res[t]<=res[v]+cost:
      continue
    res[t]=res[v]+cost
    if cost:
      dq.append(t)
    else:
      dq.appendleft(t)
print(res[0])
