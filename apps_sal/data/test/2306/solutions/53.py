N=int(input())
t=list(map(int, input().split()))
v=list(map(int, input().split()))
T=sum(t)
V=[0]*(T+2)
from collections import deque
q=[deque() for i in range(101)]
s=0
for i in range(N):
    temp=min(V[s],v[i])
    q[temp].append(s)
    for j in range(t[i]):
        V[s+j+1]=v[i]
    s+=t[i]
q[0].append(T)
vans=[-1]*(T+1)
for i in range(101):
    while(len(q[i])>0):
        s=q[i].popleft()
        if vans[s]==-1:
            vans[s]=i
        if s>0 and vans[s-1]==-1:
            if V[s]>i:
                q[i+1].append(s-1)
            else:
                q[i].append(s-1)
        if s<T and vans[s+1]==-1:
            if V[s+1]>i:
                q[i+1].append(s+1)
            else:
                q[i].append(s+1)
ans=0
for i in range(T):
    if vans[i+1]>vans[i]:
        ans+=vans[i]+0.5
    elif vans[i+1]<vans[i]:
        ans+=vans[i+1]+0.5
    elif V[i+1]>vans[i]:
        ans+=vans[i]+0.25
    else:
        ans+=vans[i]
print(ans)
