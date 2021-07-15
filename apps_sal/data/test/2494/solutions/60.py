K=int(input())

D=[K*10]*K
D[1]=1

import heapq

Q=[(1,1)]

while Q:
    c,x=heapq.heappop(Q)

    if D[x*10%K]>c:
        D[x*10%K]=c
        heapq.heappush(Q,(c,x*10%K))

    if D[(x+1)%K]>c+1:
        D[(x+1)%K]=c+1
        heapq.heappush(Q,(c+1,(x+1)%K))

print(D[0])
