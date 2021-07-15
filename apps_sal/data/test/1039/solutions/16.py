N=int(input())
G=[[] for _ in range(N)]
for _ in range(N-1):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    G[a].append([b,c])
    G[b].append([a,c])
Q,K=map(int,input().split())
K-=1
dist=[-1 for _ in range(N)]
dist[K]=0
q=[K]
while len(q)>0:
    v=q.pop()
    for p in G[v]:
        nv=p[0]
        if dist[nv]!=-1:
            continue
        dist[nv]=dist[v]+p[1]
        q.append(nv)
for _ in range(Q):
    x,y=map(int,input().split())
    print(dist[x-1]+dist[y-1])
