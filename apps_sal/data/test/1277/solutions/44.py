import sys
sys.setrecursionlimit(10**9)
f=lambda:map(int,input().split())
n,st,sa=f()
st-=1
sa-=1
g=[[] for _ in range(n)]
for _ in range(n-1):
  a,b=f()
  g[a-1].append(b-1)
  g[b-1].append(a-1)
def dfs(v,p=-1,d=0):
  l[v]=d
  for c in g[v]:
    if c==p: continue
    dfs(c,v,d+1)
def dist(s):
  nonlocal l
  l=[0]*n
  dfs(s)
  return l
lt=dist(st)
la=dist(sa)
m=0
for i in range(n):
  if lt[i]<la[i]: m=max(m,la[i])
print(m-1)
