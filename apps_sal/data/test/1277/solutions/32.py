import sys
sys.setrecursionlimit(10**7)

def dfs(v,p,d):
    dist[v]=d
    for nv in G[v]:
        if nv==p:
            continue
        dfs(nv,v,d+1)
def getSP(v):
    p=v
    if dist[v]==lim:
        return p
    for nv in G[v]:
        if dist[nv]<dist[v]:
            p=getSP(nv)
    return p
def depth(v,p,d):
    sdist[v]=d
    for nv in G[v]:
        if dist[nv]<dist[v]:
            continue
        depth(nv,v,d+1)
    
N,u,v=map(int,input().split())
u,v=u-1,v-1
G=[[] for i in range(N)]
for i in range(N-1):
    a,b=map(lambda x:int(x)-1,input().split())
    G[a].append(b)
    G[b].append(a)
dist=[-1]*N
dfs(v,-1,0)
lim=dist[u]-(dist[u]-1)//2
SP=getSP(u)
sdist=[-1]*N
depth(SP,-1,0)
D,tmp=-1,-1
for i in range(N):
    if sdist[i]>tmp:
        D=i
        tmp=sdist[i]
print(dist[D]-1)
