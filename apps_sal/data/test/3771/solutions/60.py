H,W = map(int,input().split())
A = [input() for i in range(H)]
sy = sx = ty = tx = -1
for i,row in enumerate(A):
    for j,c in enumerate(row):
        if c=='S':
            sy,sx = i,j
        if c=='T':
            ty,tx = i,j
if sy==ty or sx==tx:
    print(-1)
    return

S = H+W
G = S+1
P = G+1
es = [[] for i in range(P)] # [[to1,cap1,rev1], ...]

def add_edge(fr,to,cap):
    es[fr].append([to,cap,len(es[to])])
    es[to].append([fr,0,len(es[fr])-1])
INF = float('inf')
add_edge(S, sy, INF)
add_edge(S, H+sx, INF)
add_edge(ty, G, INF)
add_edge(H+tx, G, INF)
for i,row in enumerate(A):
    for j,c in enumerate(row):
        if c!='o': continue
        add_edge(i, H+j, 1)
        add_edge(H+j, i, 1)

level = [0] * P
iters = [0] * P
from collections import deque
def dinic_max_flow(s,t):
    nonlocal iters

    def _bfs(s):
        nonlocal level
        level = [-1] * P
        level[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for to,cap,rev in es[v]:
                if cap > 0 and level[to] < 0:
                    level[to] = level[v] + 1
                    q.append(to)

    def _dfs(v,t,f):
        if v == t: return f
        for i in range(iters[v],len(es[v])):
            iters[v] += 1
            to,cap,rev = es[v][i]
            if es[v][i][1] > 0 and level[v] < level[to]:
                d = _dfs(to,t,min(f,es[v][i][1]))
                if d > 0:
                    es[v][i][1] -= d #cap
                    es[to][rev][1] += d
                    return d
        return 0

    flow = 0
    while True:
        _bfs(s)
        if level[t] < 0: return flow
        iters = [0] * P
        f = 0
        while True:
            f = _dfs(s,t,INF)
            if f <= 0: break
            flow += f

print(dinic_max_flow(S,G))
