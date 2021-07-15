import heapq
K=int(input())
G=[[((i+1)%K,1)] for i in range(K)]
for i in range(K):
    a=(i*10)%K
    G[i].append((a,0))
def dijkstra(G,s):#Gはi->jの辺をG[i]=[(j,cost),...]で保存
  INF=10**19
  n=len(G)
  d=[INF]*n#n=node数
  d[s]=0
  visited={s}
  que=[(0,s)]
  while(que):
    p=heapq.heappop(que)
    v=p[1]
    visited.add(v)
    for node,cost in G[v]:
      if (node not in visited) and d[node]>d[v]+cost:
        d[node]=d[v]+cost
        heapq.heappush(que,(d[node],node))
  return d

d=dijkstra(G,1)
print((d[0]+1))

