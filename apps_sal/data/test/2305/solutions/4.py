import sys

input=sys.stdin.readline
sys.setrecursionlimit(10**7)

N=int(input())
c=list(map(int,input().split()))
for i in range(N):
    c[i]-=1
edge=[[] for i in range(N)]
for i in range(N-1):
    a,b=map(int,input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

subtree=[1]*N
def size(v,pv):
    for nv in edge[v]:
        if nv!=pv:
            size(nv,v)
            subtree[v]+=subtree[nv]

size(0,-1)

data=[[] for i in range(N)]
Parent=[[0] for i in range(N)]
parent=[0]*N
def dfs(v,pv,nop):
    pp=parent[nop]
    parent[nop]=v
    Parent[nop].append(v)
    data[c[v]].append((parent[c[v]],v))
    for nv in edge[v]:
        if nv!=pv:
            dfs(nv,v,c[v])
    parent[nop]=pp

dfs(0,-1,0)

for i in range(N):
    dic={v:subtree[v] for v in Parent[i]}
    for p,ch in data[i]:
        dic[p]-=subtree[ch]

    res=N*(N+1)//2
    for p in dic:
        res-=dic[p]*(dic[p]+1)//2
    print(res)
