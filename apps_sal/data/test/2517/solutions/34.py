n,m,r_=list(map(int,input().split()))
r=list(map(int,input().split()))
g=[[]for _ in range(n)]
for _ in range(m):
  a,b,c=list(map(int,input().split()))
  a-=1
  b-=1
  g[a].append([b,c])
  g[b].append([a,c])
from heapq import heapify,heappush,heappop
def dks(t0,t1):
  kyori=[-1]*n
  todo=[[0,t0]]
  heapify(todo)
  while todo:
    d,t=heappop(todo)
    kyori[t]=d
    if t==t1:break
    l=g[t]
    for li,c in l:
      if kyori[li]==-1:
        heappush(todo,[c+d,li])
  return kyori[t1]
ans=pow(10,9)
allr=[]
import sys
sys.setrecursionlimit(10**7)
def dfs(s,k): #s:list, k:set
  if len(k)==1:
    s.append(k.pop())
    return [s]
  ret=[]
  for ki in k:
    ret.extend(dfs(s+[ki],k-{ki}))
  return ret
allr=dfs([],set(r))
d={}
for i in range(r_-1):
  for j in range(i+1,r_):
    k=dks(r[i]-1,r[j]-1)
    d[r[i]-1,r[j]-1]=k
    d[r[j]-1,r[i]-1]=k

for j in range(len(allr)):
  r1=allr[j]
  ansi=0
  for i in range(r_-1):
    ansi+=d[(r1[i]-1,r1[i+1]-1)]
  ans=min(ans,ansi)
print(ans)

