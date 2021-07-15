n,k=list(map(int,input().split()))
g=[[] for _ in range(n+1)]

for i in range(n-1):
    u,v,c=list(map(int,input().split()))
    if c==0:
        g[u].append(v)
        g[v].append(u)
mod=10**9+7
def cal_pow(a,b):
    nonlocal mod
    i=0
    val=1
    while i<b:
        val=(val*a)%mod
        i+=1
    return (val-a+mod)%mod

summ=cal_pow(n,k)
vis=[False for _ in range(n+1)]
from collections import deque
def bfs(ind):
    q=deque()
    q.append(ind)
    cnt=0
    vis[ind]=True
    while q:
        indx=q.popleft()
        cnt+=1
        for v in g[indx]:
            if not vis[v]:
                q.append(v)
                vis[v]=True
    return cnt

for v in range(1,n+1):
    if not vis[v]:
        cnt=bfs(v)
        summ=((mod+summ)-(cal_pow(cnt,k)))%mod
print(summ)


