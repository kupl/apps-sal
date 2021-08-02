import random
import sys
from collections import deque
from heapq import heappop, heappush


class Edge(object):
    __slots__ = ('x', 'y', 'cap', 'cost', 'inv')

    def __repr__(self):
        return '{e.x}-->{e.y} ({e.cap} , {e.cost})'.format(e=self)


class MCFP(list):
    def add(G, x, y, cap, cost):
        n = max(x, y) + 1
        while len(G) < n: G.append([])
        e = Edge(); G[x].append(e)
        w = Edge(); G[y].append(w)
        e.x = x; e.y = y; e.cap = cap; e.cost = cost; w.inv = e
        w.x = y; w.y = x; w.cap = 0; w.cost = -cost; e.inv = w

    def solve(G, src, tgt, flowStop=float('inf'), inf=float('inf')):
        flowVal = flowCost = 0
        n = len(G)
        G.inQ = [0] * n
        G.phi = h = [0] * n
        G.prev = p = [None] * n
        G.dist = d = [inf] * n
        G.SPFA(src)
        while p[tgt] != None and flowVal < flowStop:
            b = []; x = tgt
            while x != src: b.append(p[x]); x = p[x].x
            z = min(e.cap for e in b)
            for e in b: e.cap -= z; e.inv.cap += z
            flowVal += z
            flowCost += z * (d[tgt] - h[src] + h[tgt])
            for i in range(n):
                if p[i] != None: h[i] += d[i]; d[i] = inf
            p[tgt] = None
            G.SPFA(src)
        return flowVal, flowCost

    def SPFA(G, src):
        inQ = G.inQ; prev = G.prev
        d = G.dist; h = G.phi
        d[src] = 0
        Q = deque([src])
        while Q:
            x = Q.popleft()
            inQ[x] = 0
            for e in G[x]:
                if e.cap <= 0: continue
                y = e.y; dy = d[x] + h[x] + e.cost - h[y]
                if dy < d[y]:
                    d[y] = dy; prev[y] = e
                    if inQ[y] == 0:
                        inQ[y] = 1
                        if not Q or dy > d[Q[0]]: Q.append(y)
                        else: Q.appendleft(y)
        return


ints = (int(x) for x in sys.stdin.read().split())
sys.setrecursionlimit(3000)


def main():
    n, k = (next(ints) for i in range(2))
    a = [next(ints) for i in range(n)]
    b = [next(ints) for i in range(n)]
    G = MCFP()
    src, tgt = 2 * n + 1, 2 * n + 2
    for i in range(n):
        G.add(src, i, 1, 0)
        G.add(i, i + n, 1, a[i])
        G.add(i + n, tgt, 1, b[i])
        if i + 1 < n:
            G.add(i, i + 1, n, 0)
            G.add(i + n, i + n + 1, n, 0)
    flowVal, ans = G.solve(src, tgt, k)
    assert flowVal == k
    print(ans)
    # print(G)
    return


def test(n, k):
    R = random.Random(0)
    yield n; yield k
    for i in range(n): yield R.randint(1, 10**9)
    for i in range(n): yield R.randint(1, 10**9)

#ints=test(1000, 800)


main()
