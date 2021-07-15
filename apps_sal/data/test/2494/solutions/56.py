import heapq
K=int(input())
dist=[10**15 for i in range(K)]
dist[1]=1
q=[]
heapq.heappush(q,(0,1))
while (len(q)!=0):
    prc,src=heapq.heappop(q)
    if dist[src]<prc:
        continue
    if dist[(src+1)%K]>dist[src]+1:
        dist[(src+1)%K]=dist[src]+1
        heapq.heappush(q,(dist[(src+1)%K],(src+1)%K))
    if dist[(10*src)%K]>dist[src]:
        dist[(10*src)%K]=dist[src]
        heapq.heappush(q,(dist[(src*10)%K],(src*10)%K))
print((dist[0]))

