R = lambda : map(int, input().split())
n,m,s,t = R()

graph = [set() for _ in range(n)]
edges = set()

for _ in range(m):
    u,v = R()
    graph[u-1].add(v-1)
    graph[v-1].add(u-1)
    edges.add((u-1,v-1))
    edges.add((v-1,u-1))

from collections import deque
def bfs(v):
    q = deque()
    q.append((v,0))
    dis = {}
    while q:
        vertex = q.popleft();
        dis[vertex[0]] = vertex[1]
        for nv in graph[vertex[0]]:
            if nv not in dis:
                dis[nv] = vertex[1]+1
                q.append((nv, vertex[1]+1))
    return dis

ds = bfs(s-1)
dt = bfs(t-1)
dist = bfs(s-1)[t-1]

res = (n*(n-1))//2-m
for i in range(n):
    for j in range(i+1, n):
        if (i,j) not in edges:
            if ds[i]+dt[j]+1 < dist:
                res -= 1
            elif ds[j]+dt[i]+1 <dist:
                res -= 1

print(res)
