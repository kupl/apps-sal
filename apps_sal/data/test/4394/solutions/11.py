import sys


def get(v):
    if v == prev[v]:
        return v
    prev[v] = get(prev[v])
    return prev[v]


def join(u, v):
    u = get(u)
    v = get(v)
    if u != v:
        if size[u] < size[v]:
            (u, v) = (v, u)
        prev[v] = u
        size[u] += size[v]


(n, m) = map(int, sys.stdin.readline().split())
edges = [0] * m
for i in range(m):
    (u, v, w) = map(int, sys.stdin.readline().split())
    edges[i] = (u - 1, v - 1, w)
edges.sort(key=lambda e: e[2])
prev = list(range(n))
size = [1] * n
res = 0
(l, r) = (0, 1)
while l < m:
    while r < m and edges[l][2] == edges[r][2]:
        r += 1
    res += r - l
    for i in range(l, r):
        if get(edges[i][0]) == get(edges[i][1]):
            res -= 1
    for i in range(l, r):
        if get(edges[i][0]) != get(edges[i][1]):
            join(edges[i][0], edges[i][1])
            res -= 1
    l = r
print(res)
