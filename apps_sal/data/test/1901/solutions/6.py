from collections import deque

n,m=list(map(int,input().split()))
c=list(map(int,input().split()))
adj=[[] for _ in range(100000)]
for _ in range(m):
    x,y=list(map(int,input().split()))
    x-=1
    y-=1
    adj[x].append(y)
    adj[y].append(x)
ans=0
used=[False]*n
for i in range(n):
    if used[i]:
        continue
    s=[c[i]]
    used[i]=True
    q=deque([])
    q.append(i)
    while len(q)>0:
        u=q.popleft()
        for j in range(len(adj[u])):
            v=adj[u][j]
            if not used[v]:
                used[v]=True
                s.append(c[v])
                q.append(v)
    ans+=min(s)
print(ans)

