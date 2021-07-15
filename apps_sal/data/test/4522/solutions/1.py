from bisect import bisect
from math import inf


def union_init(s):
    d = [i for i in range(s)]
    size = [1 for i in range(s)]
    return (d, size)


def union_query(d, size, n):
    if d[n] != n:
        d[n] = union_query(d, size, d[n])
    return d[n]


def union_merge(d, size, x, y):
    xRoot = union_query(d, size, x)
    yRoot = union_query(d, size, y)

    if xRoot == yRoot:
        return
    if size[xRoot] < size[yRoot]:
        xRoot, yRoot = yRoot, xRoot
    d[yRoot] = xRoot
    size[xRoot] = size[xRoot] + size[yRoot]


def sizeComponent(d, size, x):
    root = union_query(d, size, x)
    return size[root]


nm = input().split()
n = int(nm[0])
m = int(nm[1])

d, size = union_init(n)
pairs = [(0, 0)]
edges = []
for _ in range(n - 1):
    edge = input().split()
    u = int(edge[0]) - 1
    v = int(edge[1]) - 1
    w = int(edge[2])
    edges.append((w, u, v))

edges.sort()
totalP = 0
for e in edges:
    u = e[1]
    v = e[2]
    uSize = sizeComponent(d, size, u)
    vSize = sizeComponent(d, size, v)
    totalP += uSize * vSize
    union_merge(d, size, u, v)
    pairs.append((e[0], totalP))

ms = [int(mi) for mi in input().split()]
answer = [0] * m
for i, mi in enumerate(ms):
    start = bisect(pairs, (mi, inf)) - 1
    answer[i] = pairs[start][1]
print(*answer)

