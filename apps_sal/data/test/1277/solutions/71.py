import sys
sys.setrecursionlimit(10**6)
 
N,u,v = map(int,input().split())
edges = [list(map(int,input().split())) for _ in range(N-1)]
E = [[] for _ in range(N+1)]
for a,b in edges:
    E[a].append(b)
    E[b].append(a)
 
depth = [[-1,-1] for _ in range(N+1)] 
depth[v][0] = 0
depth[u][1] = 0

def dfs1(E,v):
    vv = E[v]
    for vvv in vv:
        if depth[vvv][0] == -1:
            depth[vvv][0] = depth[v][0] + 1
            dfs1(E,vvv)
 
def dfs2(E,v):
    vv = E[v]
    for vvv in vv:
        if depth[vvv][1] == -1:
            depth[vvv][1] = depth[v][1] + 1
            dfs2(E,vvv)
dfs1(E,v)
dfs2(E,u)
depth = sorted(depth, reverse=True)
idx = 0
while True:
    if depth[idx][0] - depth[idx][1] >= 1:
        print(depth[idx][0]-1)
        return
    else:
        idx += 1
