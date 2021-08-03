import sys
from collections import deque
from heapq import heappop, heappush


class Edge(object):
    __slots__ = ('x', 'y', 'cap', 'cost', 'inv')

    def __repr__(self):
        return f'{self.x}-->{self.y} ({self.cap} , {self.cost})'


class MCFP():
    def __init__(self):
        self.G = []

    def add(self, x, y, cap, cost):
        G = self.G
        G.extend(([] for i in range(max(0, max(x, y) + 1 - len(G)))))
        e = Edge()
        e.x = x
        e.y = y
        e.cap = cap
        e.cost = cost
        z = Edge()
        z.x = y
        z.y = x
        z.cap = 0
        z.cost = -cost
        e.inv = z
        z.inv = e
        G[x].append(e)
        G[y].append(z)

    def solve(self, src, tgt, inf=float('inf')):
        n, G = len(self.G), self.G
        flowVal = flowCost = 0
        phi = [0] * n
        prev = [None] * n
        inQ = [0] * n
        cntQ = 1
        dist = [inf] * n
        while 1:
            self.shortest(src, phi, prev, inQ, dist, inf, cntQ)
            if prev[tgt] == None:
                break
            z = inf
            x = tgt
            while x != src:
                e = prev[x]
                z = min(z, e.cap)
                x = e.x
            x = tgt
            while x != src:
                e = prev[x]
                e.cap -= z
                e.inv.cap += z
                x = e.x
            flowVal += z
            flowCost += z * (dist[tgt] - phi[src] + phi[tgt])
            for i in range(n):
                if prev[i] != None:
                    phi[i] += dist[i]
                    dist[i] = inf
            cntQ += 1
            prev[tgt] = None
        return flowVal, flowCost

    def shortest(self, src, phi, prev, inQ, dist, inf, cntQ):
        n, G = len(self.G), self.G
        Q = [(dist[src], src)]
        inQ[src] = cntQ
        dist[src] = 0
        while Q:
            _, x = heappop(Q)
            inQ[x] = 0
            dx = dist[x] + phi[x]
            for e in G[x]:
                y = e.y
                dy = dx + e.cost - phi[y]
                if e.cap > 0 and dy < dist[y]:
                    dist[y] = dy
                    prev[y] = e
                    if inQ[y] != cntQ:
                        inQ[y] = cntQ
                        heappush(Q, (dy, y))
        return dist, prev

    def __repr__(self):
        n, G = len(self.G), self.G
        s = []
        for i in range(n):
            s.append('    G[{}]:'.format(i))
            s.append('\n'.join('        {}'.format(e) for e in G[i]))
        return '\n'.join(s)


ints = (int(x) for x in sys.stdin.read().split())
sys.setrecursionlimit(3000)


def main():
    n, q = (next(ints) for i in range(2))
    leq = [n - 1] * n
    geq = [0] * n
    for q in range(q):
        t, l, r, v = (next(ints) for i in range(4))
        for i in range(l - 1, r):
            if t == 1:
                geq[i] = max(geq[i], v - 1)
            if t == 2:
                leq[i] = min(leq[i], v - 1)
    imp = any(geq[i] > leq[i] for i in range(n))
    if imp:
        ans = -1
    else:
        src = 2 * n + n * n
        tgt = 2 * n + n * n + 1
        G = MCFP()
        for i in range(n):
            G.add(src, i, 1, 0)
        for i in range(n):
            for j in range(geq[i], leq[i] + 1):
                G.add(i, j + n, 1, 0)
        for i in range(n):
            for j in range(n):
                G.add(i + n, 2 * n + i * n + j, 1, 0)
                G.add(2 * n + i * n + j, tgt, 1, 2 * j + 1)
        _, ans = G.solve(src, tgt)
        # print(G)
        #print(leq, geq)
    print(ans)
    return


main()
