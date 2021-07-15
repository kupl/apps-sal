n,m=list(map(int,input().split()))
G=[[] for i in range(n)]
for i in range(m):
  l,r,d=list(map(int,input().split()))
  G[l-1].append([r-1,d])
  G[r-1].append([l-1,-d])

dist=[None]*n
from collections import deque
for i in range(n):
  q=deque()
  if dist[i]==None:
    dist[i]=0
    q.append(i)
  while q:
    cur=q.popleft()
    for nx,nxd in G[cur]:
      if dist[nx]==None:
        dist[nx]=dist[cur]+nxd
        q.append(nx)
      elif dist[nx]!=dist[cur]+nxd:
        print("No")
        return
print("Yes")


