import sys
from collections import deque
def serp(s):
  prev = [-1]*n
  q=deque([s])
  while q:
    v = q.pop()
    for nv in e[v]:
      if nv==s: prev[nv]=v; return(s,prev)
      if prev[nv]<0: q+=nv,; prev[nv] =v
  return(-1,prev)
n,m,*t=map(int,open(0).read().split())
e,ab = [[] for i in range(n)],[]
for a,b in zip(*[iter(t)]*2):
  e[a-1]+= b-1,
  ab += [(a-1,b-1)]
for v in range(n):
  v0,prev = serp(v)
  if v0>=0: break
if v0<0: print(-1); return
c=set()
c.add(v0)
pv = prev[v0]
while pv!=v0:
  c.add(pv)
  pv=prev[pv]
for a,b in ab:
  if a in c and b in c and prev[b]!=a:
    pv = prev[b]
    while pv !=a:
      c.remove(pv)
      pv=prev[pv]
    prev[b]=a
print(len(c))
for i in c: print(i+1)
