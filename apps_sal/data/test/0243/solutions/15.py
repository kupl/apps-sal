import sys
input = sys.stdin.readline

# def find(a):
#     if par[a] == a:
#         return a
#     par[a] = find(par[a])
#     return par[a]

def find(a):
    upd = []
    cur = a
    while par[cur] != cur:
        upd.append(cur)
        cur = par[cur]
    for x in upd:
        par[x] = cur
    return cur

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    par[a] = b


def mst():
    ret = []
    for edge in edges:
        u, v, w = edge
        u = find(u)
        v = find(v)
        if u != v:
            union(u, v)
            ret.append(edge)
    return ret


def dfs(u, par):
    for v, w in adj[u]:
        if v != par:
            dist[v] = max(dist[u], w)
            dfs(v, u)

def bfs(u):
    visit = [False] * (n+1)
    from collections import deque

    dq = deque()
    dq.append(u)
    visit[u] = True
    while dq:
        u = dq.popleft()
        for v, w in adj[u]:
            if not visit[v]:
                dist[v] = max(dist[u], w)
                dq.append(v)
                visit[v] = True


n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
# n = 50000
# m = 2 * n
# k = n
# a = [i for i in range(1, n+1)]
# import random

par = [0] * (n+1)
for i in range(1, n+1):
    par[i] = i
edges = []
# for i in range(1, n+1):
#     edge = (i, 1 if i+1 > n else i+1, random.randint(1, 1000000000))
#     edge = (i, 1 if i+2 > n else i+2, random.randint(1, 1000000000))
#     edges.append(edge)
for i in range(m):
    edge = tuple(map(int, input().split()))
    edges.append(edge)
edges.sort(key=lambda x: x[2])
edges = mst()
adj = [list() for i in range(n+1)]
for edge in edges:
    u, v, w = edge
    adj[u].append((v, w))
    adj[v].append((u, w))

dist = [0] * (n+1)
# dfs(a[0], -1)
bfs(a[0])
ans = 0
for x in a:
    ans = max(ans, dist[x])
ans = [ans] * k
print(*ans)


