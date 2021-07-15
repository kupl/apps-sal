#Hopscotch Addict

N,M=list(map(int,input().split()))
graph={(i,j):[] for i in range(1,N+1) for j in range(1,4)}
for _ in range(M):
    u,v=list(map(int,input().split()))
    graph[(u,1)].append((v,2))
    graph[(u,2)].append((v,3))
    graph[(u,3)].append((v,1))
S,T=list(map(int,input().split()))

import heapq
def dijkstra(s,graph):
    dist={(i,j):float("inf") for i in range(1,N+1) for j in range(1,4)}
    dist[(s,3)]=0
    pq=[]
    heapq.heapify(pq)
    heapq.heappush(pq,(0,(s,3)))
    while pq:
        x=heapq.heappop(pq)
        node,mini_dis=x[1],x[0]
        for next_node in graph[node]:
            newlen=dist[node]+1
            if newlen<dist[next_node]:
                heapq.heappush(pq,(newlen,next_node))
                dist[next_node]=newlen
    return dist
K=dijkstra(S,graph)[(T,3)]
if K==float("inf"):
    print((-1))
else:
    print((K//3))


