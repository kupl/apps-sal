N,M,S=map(int,input().split())
from heapq import heappop,heappush 

inf = float('inf')
cost=[[] for _ in range(N)]
exc=[]


for _ in range(M):
    u,v,a,b=map(int,input().split())
    u,v=u-1,v-1
    cost[u].append((v,a,b))
    cost[v].append((u,a,b))
for _ in range(N):
    c,d=map(int,input().split())
    exc.append((c,d))

di=[inf]*2451*N
if S>2450:
    S=2450
di[S]=0
hq=[(0,S)] #時間,都市名*2451+銀貨

while hq:
    t,v=heappop(hq)
    u=v//2451 #都市名
    s=v%2451 #所持金

    for x,a,b in cost[u]:
        if s>=a:
            v_new=x*2451+s-a
            t_new=t+b
            if t_new<di[v_new]:
                di[v_new]=t_new
                heappush(hq,(t_new,v_new))
    
    c,d=exc[u]
    if s+c>2450:
        c=2450-s
    v_new=v+c
    t_new=t+d
    if t_new<di[v_new]:
        di[v_new]=t_new
        heappush(hq,(t_new,v_new))

for i in range(1,N):
    m=di[i*2451]
    for j in range(1,2451):
        m=min(m,di[i*2451+j])
    print(m)
