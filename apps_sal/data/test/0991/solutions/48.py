#拡張ダイクストラ 
#weight,point
N,M,S=map(int,input().split())
graph={(i,j):[] for i in range(1,51) for j in range(2501)}
for _ in range(M):
    u,v,a,b=map(int,input().split())
    for i in range(a,2501):
        graph[(u,i)].append((b,(v,i-a)))
        graph[(v,i)].append((b,(u,i-a)))
for i in range(N):
    c,d=map(int,input().split())
    for j in range(2501):
        graph[(i+1,j)].append((d,(i+1,min(2500,j+c))))

dist={(i,j):float("inf")  for i in range(1,51) for j in range(2501)}

dist[(1,min(2500,S))]=0
pq=[]
import heapq
heapq.heapify(pq)
heapq.heappush(pq,(0,(1,min(2500,S))))
while pq:
    mini_dis,node=heapq.heappop(pq)
    if dist[node]<mini_dis: continue
    for w,point in graph[node]:
        if dist[point]<w:continue
        newlen=dist[node]+w
        if newlen<dist[point]:
            heapq.heappush(pq,(newlen,point))
            dist[point]=newlen
for i in range(2,N+1):
    ans=10**20
    for j in range(2501):
        ans=min(ans,dist[(i,j)])
    print(ans)
