import sys
import itertools
import bisect
input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))
edges=[list(map(int,input().split())) for _ in range(m)]
edges.append([0,0])
edges=sorted(edges,key=lambda x:x[0])
ls=[]
ws=[]
for i in range(m-1,-1,-1):
  edges[i][1]=min(edges[i][1],edges[i+1][1])
for l,w in edges:
  ls.append(l)
  ws.append(w)
if max(arr)>ws[1]:
  print(-1)
  return
ans=10**18
for p in itertools.permutations(range(n)):
  tmp=[0]*n
  for i in range(n):
    tmp[i]=arr[p[i]]
  tans=[0]*(n-1)
  for r in range(1,n):
    for l in range(0,r):
      w=sum(tmp[l:r+1])
      pos=bisect.bisect_left(ws,w)
      tans[r-1]=max(tans[r-1],ls[pos-1]-sum(tans[l:r-1]))
  ans=min(ans,sum(tans))
print(ans)
