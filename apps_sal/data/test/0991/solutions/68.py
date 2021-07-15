import math
import heapq

n,m,s = map(int,input().split())

road = []
for i in range(m):
    u,v,a,b = map(int,input().split())
    road.append([u,v,a,b])

change = []
for i in range(n):
    c,d = map(int,input().split())
    change.append([c,d])

tree = [[] for _ in range(n+1)]

for i in range(m):  
    r = road[i]
    tree[r[0]].append([r[0],r[1],r[2],r[3]])
    tree[r[1]].append([r[1],r[0],r[2],r[3]])

least_cost = [[] for _ in range(n+1)]
for l in range(n+1):
    least_cost[l] = [math.inf]*2501

queue = []

#hwd [location, money, time]
def dijakstra(q):
    while q != []:
        hwd = heapq.heappop(q)

        if least_cost[hwd[1]][hwd[2]] > hwd[0]:
            least_cost[hwd[1]][hwd[2]] = hwd[0]
            
            for node in tree[hwd[1]]:
                # from node, to node , money, time
                if hwd[2] - node[2] >= 0:
                    heapq.heappush(q,(hwd[0]+node[3],node[1],hwd[2]-node[2]))
            if hwd[2] + change[hwd[1]-1][0] <= 2500:
                heapq.heappush(q,(hwd[0]+change[hwd[1]-1][1],hwd[1],hwd[2]+change[hwd[1]-1][0]))
    return least_cost

if s > 2500:
    s = 2500
queue.append((0,1,s))

ans = dijakstra(queue)

for i in range(2,n+1):
    print(min(ans[i]))
