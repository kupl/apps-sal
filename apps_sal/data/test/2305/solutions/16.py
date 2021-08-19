from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


class Graph(object):

    def __init__(self, N):
        self.N = N
        self.E = defaultdict(list)

    def add_edge(self, f, t, w=1):
        self.E[f].append((t, w))
        self.E[t].append((f, w))


N = int(input())
c = [x - 1 for x in map(int, input().split())]
A = [None] * (N - 1)
B = [None] * (N - 1)
for i in range(N - 1):
    (A[i], B[i]) = list(map(int, input().split()))
g = Graph(N)
for (a, b) in zip(A, B):
    g.add_edge(a - 1, b - 1)
ans = [0] * N


def f(curr, par=-1):
    ret = defaultdict(int)
    size = 1
    for (dest, w) in g.E[curr]:
        if dest == par:
            continue
        (sz, child) = f(dest, curr)
        size += sz
        n = sz - child[c[curr]]
        ans[c[curr]] += n * (n + 1) // 2
        if len(ret) < len(child):
            (child, ret) = (ret, child)
        for key in child:
            ret[key] += child[key]
    ret[c[curr]] = size
    return (size, ret)


(sz, ret) = f(0)
for color in range(N):
    if color != c[0]:
        n = sz - ret[color]
        ans[color] += n * (n + 1) // 2
tot = N * (N + 1) // 2
for a in ans:
    print(tot - a)
