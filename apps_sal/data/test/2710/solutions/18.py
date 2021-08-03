from sys import stdin, stdout, stderr
from collections import deque

n, m = list(map(int, stdin.readline().split()))
ai = [int(x) for x in stdin.readline().split()]
bi = [int(x) for x in stdin.readline().split()]

N = 2 * n + 2
M = 4 * m + 6 * n
cap = [None for i in range(M)]
flow = [0 for i in range(M)]
adj = [[] for i in range(N)]
L = []
cure = []

s = 0
t = 2 * n + 1

INF = 0x3f3f3f3f


def bfs():
    nonlocal L, cure
    L = [INF for i in range(N)]
    cure = [0 for i in range(N)]
    q = deque()
    q.append(s)
    L[s] = 0
    while q:
        u = q.pop()
        for v, e in adj[u]:
            if flow[e] < cap[e] and L[v] == INF:
                q.append(v)
                L[v] = L[u] + 1
    return L[t] < INF


def dfs(u, f):
    if u == t:
        return f
    pushed = 0
    lim = len(adj[u])
    while cure[u] < lim:
        v, e = adj[u][cure[u]]
        if flow[e] < cap[e] and L[v] == L[u] + 1:
            cur = dfs(v, min(cap[e] - flow[e], f - pushed))
            flow[e] += cur
            flow[e ^ 1] -= cur
            pushed += cur
        if pushed == f:
            break
        cure[u] += 1
    return pushed


eid = 0


def add_edge(a, b, c):
    nonlocal eid, adj, cap
    adj[a].append((b, eid))
    cap[eid] = c
    eid += 1


for i in range(m):
    a, b = list(map(int, stdin.readline().split()))
    add_edge(a, n + b, INF)
    add_edge(n + b, a, 0)
    add_edge(b, n + a, INF)
    add_edge(n + a, b, 0)
for i in range(n):
    add_edge(s, i + 1, ai[i])
    add_edge(i + 1, s, 0)
    add_edge(n + i + 1, t, bi[i])
    add_edge(t, n + i + 1, 0)
    add_edge(i + 1, n + i + 1, INF)
    add_edge(n + i + 1, i + 1, 0)

ans = 0
while bfs():
    ans += dfs(s, INF)

if ans != sum(ai) or ans != sum(bi):
    stdout.write('NO\n')
else:
    stdout.write('YES\n')
    grid = [[0 for j in range(n)] for i in range(n)]
    for u in range(1, n + 1):
        for v, e in adj[u]:
            if flow[e] > 0 and 1 <= v - n and v - n <= n:
                grid[u - 1][v - n - 1] += flow[e]
    stdout.write('\n'.join([' '.join([str(x) for x in line]) for line in grid]) + '\n')
