import sys
input=sys.stdin.readline
from collections import defaultdict as dd,deque as dq
def bfs(vis,u,d):
    l=[]
    q=dq([u])
    while q:
        u=q.popleft()
        vis[u]=1
        l.append(u)
        for j in d[u]:
            if(vis[j]==-1):
                
                q.append(j)
    return (min(l),max(l))
n,m=map(int,input().split())
d=dd(list)

while m:
    u,v=map(int,input().split())
    d[u].append(v)
    d[v].append(u)
    m-=1
vis=[-1]*(n+1)
seg=[]
for i in range(1,n+1):
    if(vis[i]==-1):
        seg.append(bfs(vis,i,d))
seg.sort()
mi=seg[0][0]
mx=seg[0][1]
cou=0
for i in range(1,len(seg)):
    if(seg[i][0]>=mi and seg[i][0]<=mx):
        cou+=1
        mx=max(seg[i][1],mx)
    else:
        mx=max(seg[i][1],mx)
print(cou)
