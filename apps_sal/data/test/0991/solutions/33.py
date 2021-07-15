from collections import defaultdict
import heapq
N,M,S = list(map(int,input().split()))
E=[list(map(int,input().split())) for _ in range(M)]

C=[list(map(int,input().split())) for _ in range(N)]

A_max=max([a for _,_,a,_ in E])*N

D=defaultdict(lambda :[])

for u,v,a,b in E:
    u-=1;v-=1
    for from_a in range(A_max+1):
        if from_a-a<0:
            continue
        from_state_u=(u,from_a)
        to_state_v=(v,from_a-a)
        D[from_state_u].append((b,to_state_v))

        from_state_v=(v,from_a)
        to_state_u=(u,from_a-a)
        D[from_state_v].append((b,to_state_u))

for n,[c,d] in enumerate(C):
    for a in range(A_max+1):
        a_after=min(A_max,a+c)
        from_state=(n,a)
        to_state=(n,a_after)
        D[from_state].append((d,to_state))


start=(0,min(A_max,S))
Q=[(0,start)]

Dist=defaultdict(lambda :float('inf'))

Dist[start]=0

while Q:
    q = heapq.heappop(Q)
    cur_time,cur_state=q

    if Dist[cur_state]<cur_time:
        continue
    for cost,next_state in D[cur_state]:
        next_time = cost+cur_time

        if Dist[next_state]>next_time:
            Dist[next_state]=next_time
            heapq.heappush(Q,(next_time,next_state))

for dest in range(1,N):
    ans=float("inf")
    for a in range(A_max+1):
        state=(dest,a)
        ans=min(ans,Dist[state])
    print(ans)

