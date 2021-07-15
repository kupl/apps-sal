from heapq import heappop,heappush
def dijkstra(s,n,edge):
  inf=10**20
  ans=[inf]*n
  ans[s]=0
  h=[[0,s]]
  while h:
    c,v=heappop(h)
    if ans[v]<c:continue
    for u,t in edge[v]:
      if c+t<ans[u]:
        ans[u]=c+t
        heappush(h,[c+t,u])
  return ans
k=int(input())
edge=[[]for _ in range(k)]
for i in range(1,k):
    edge[i].append(((i*10)%k,0))
    edge[i].append(((i+1)%k,1))
ans=dijkstra(1,k,edge)
print((ans[0]+1))

