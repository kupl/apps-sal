from sys import stdin
from collections import deque

def bfs(G, s):
    Q = deque()
    Q.append(s)
    infinite = 10 ** 6
    d = [infinite]*n
    d[s] = 0
    while Q:
        u = Q.popleft()
        for v in graph[u]:
            if d[v] == infinite:
                d[v] = d[u] + 1
                Q.append(v)
    return d

n, x = list(map(int, stdin.readline().split()))
x = x - 1

graph = [[] for i in range(n)]
for i in range(n - 1):
    a, b = list(map(int, stdin.readline().split()))
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

d_Alice = bfs(graph, 0)
d_Bob = bfs(graph, x)

resp = d_Alice[x]
for i,v in enumerate(graph):
    if len(v) == 1 and d_Alice[i] > d_Bob[i]:
        resp = max(resp, d_Alice[i])
print(2*resp)

