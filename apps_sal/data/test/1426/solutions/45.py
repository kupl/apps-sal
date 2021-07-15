import heapq
N,M = map(int,input().split())

edge = [[] for _ in range(N)]
for _ in range(M):
    u,v = map(int,input().split())
    u,v = u-1,v-1
    edge[u].append(v)
    
S,T = map(int,input().split())
S,T = S-1,T-1


INF = N*3

dist = [[INF]*3 for _ in range(N)]

dist[S][0] = 0

q = [(0,S)]

while q:
    d, vs = heapq.heappop(q)
    if d > dist[vs][d%3]: continue
    
    for ve in edge[vs]:
        lev = (d+1)%3
        if d+1 < dist[ve][lev]:
            dist[ve][lev] = d+1
            heapq.heappush(q,(d+1,ve))
    
    if dist[T][0] < INF: break
        
print(dist[T][0]//3 if dist[T][0]<INF else -1)
