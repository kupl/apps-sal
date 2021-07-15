import heapq
a,b,x,y = map(int,input().split())
G = {}
for i in range(1,101):
    G[(0,i)]=[]
    if i-1>=1:
        G[(0,i)].append((0,i-1,y))
        G[(0,i)].append((1,i-1,x))
    if i+1<=100:
        G[(0,i)].append((0,i+1,y))
    G[(0,i)].append((1,i,x))
    G[(1,i)]=[]
    if i-1>=1:
        G[(1,i)].append((1,i-1,y))
    if i+1<=100:
        G[(1,i)].append((1,i+1,y))
        G[(1,i)].append((0,i+1,x))
    G[(1,i)].append((0,i,x))
dist = {}
INFTY = 30000
for i in range(1,101):
    dist[(0,i)]=INFTY
    dist[(1,i)]=INFTY
hist = {}
for i in range(1,101):
    hist[(0,i)]=0
    hist[(1,i)]=0
heap = [(0,(0,a))]
dist[(0,a)]=0
hist[(0,a)]=1
while heap:
    d,x = heapq.heappop(heap)
    if dist[x]<d:continue
    hist[x]=1
    for i,j,dy in G[x]:
        y = (i,j)
        if hist[y]==0 and dist[y]>d+dy:
            dist[y]=d+dy
            heapq.heappush(heap,(d+dy,y))
print(dist[(1,b)])
