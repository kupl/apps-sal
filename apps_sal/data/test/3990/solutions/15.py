def bfs(g,n):
    q=[1]
    vis=[1 for x in range(n+1)]
    dis=[0 for x in range(n+1)]
    while len(q):
        cur=q[0]
        q.remove(cur)
        for i in g[cur]:
            if vis[i]:
                q.append(i)
                vis[i]=0
                dis[i]=dis[cur]+1
                if i==n:
                    return dis[n]
    return -1
        

[n,m]=[int(x) for x in input().split()]
rag=[[] for x in range(n+1)]
rog=[[] for x in range(n+1)]
for i in range(m):
    [a,b]=[int(x) for x in input().split()]
    rag[a].append(b)
    rag[b].append(a)
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if j not in rag[i]:
            rog[i].append(j)
            rog[j].append(i)
if n in rag[1]:
    print(bfs(rog,n))
else:
    print(bfs(rag,n))

