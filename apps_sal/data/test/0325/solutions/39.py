def BF(v, start, edges):
    INF = 10**18
    nega = False
    d = [INF] * v
    d[start] = 0
    for _ in range(v):
        f = False
        for a, b, c in edges:
            cost = d[a] + c
            if cost < d[b]:
                d[b] = cost
                f = True
        if not f:
            break
    else:
        nega = True
    return d, nega

from collections import deque
def BFS(N, graph, start):
    d = [-1 for i in range(N)]
    Q = deque([])
    Q.append(start)
    d[start] = 0
    while Q:
        v = Q.popleft()
        for u in graph[v]:
            if d[u] == -1:
                d[u] = d[v] + 1
                Q.append(u)
    return d

N, M, P = (int(i) for i in input().split())
graph = [[] for i in range(N)]
graphr = [[] for i in range(N)]
edges = []
for i in range(M):
    A, B, C = (int(i) for i in input().split())
    graph[A-1].append(B-1)
    graphr[B-1].append(A-1)
    edges.append((A-1, B-1, P-C))
d_start = BFS(N, graph, 0)
d_end = BFS(N, graphr, N-1)
nodes_start = [i for i in range(N) if d_start[i] >= 0]
nodes_end = [i for i in range(N) if d_end[i] >= 0]
new_edges = []
for A, B, C in edges:
    if A in nodes_start and B in nodes_start and A in nodes_end and B in nodes_end:
        new_edges.append((A, B, C))
d, Nega = BF(N, 0, new_edges)
if Nega == True:
    print(-1)
else:
    print(max(-d[N-1], 0))
