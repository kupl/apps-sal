import sys
INF=float('inf')
def Bellmanford(n,edges,r):
  d=[INF]*n
  d[r]=0    
  for i in range(n):
    for (u,v,c) in edges:
      if d[u]!=INF and d[u]+c<d[v]:
        d[v]=d[u]+c
        if i==n-1 and v==n-1:
          return 'inf'   
  return (-1)*d[n-1]

N,M=list(map(int, sys.stdin.readline().split()))
Edges=[0]*M

for i in range(M):
  a,b,c=list(map(int, sys.stdin.readline().split()))
  Edges[i]=(a-1,b-1,-c)
    
ans=Bellmanford(N,Edges,0)
print(ans)

