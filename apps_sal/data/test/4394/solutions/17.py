import collections as cc
import itertools as it
import bisect as bi
def I(): return list(map(int, input().split()))


n, m = I()
ed = [I() for i in range(m)]
ed.sort(key=lambda x: x[2])
ch = []
for i in range(1, m):
    if ed[i - 1][2] != ed[i][2]:
        ch.append(i)
ch.append(m)
parent = [i for i in range(n + 1)]


def find(x):
    while x != parent[x]:
        x = parent[x]
    return x


def union(x, y):
    a = find(x)
    b = find(y)
    parent[a] = parent[b] = min(a, b)


cur = 0

cur = 0
no = [0] * m
ans = 0
for i in ch:
    for j in range(cur, i):
        if find(ed[j][0]) == find(ed[j][1]):
            no[j] = 1
    for j in range(cur, i):
        if no[j] == 1:
            continue
        x, y, w = ed[j]
        if find(x) != find(y):
            union(x, y)
        else:
            ans += 1
    cur = i


print(ans)
