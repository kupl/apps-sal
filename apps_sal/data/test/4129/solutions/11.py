import sys


def d(u):
    rt[u] = False
    for v in q[u]:
        if rt[v]:
            d(v)
    topo.append(u)


sys.setrecursionlimit(6000)
n, m, s = map(int, input().split())
q = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    q[u - 1].append(v - 1)
rt, topo = [True] * n, []
for i, a in enumerate(rt):
    if a:
        d(i)
rt, res = [True] * n, 0
d(s - 1)
for i in reversed(topo):
    if rt[i]:
        res += 1
        d(i)
print(res)
