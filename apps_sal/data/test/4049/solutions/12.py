from heapq import heappop as hpp, heappush as hp
import sys
readline = sys.stdin.readline


class MinCostFlowwithDijkstra:
    INF = 1 << 60

    def __init__(self, N):
        self.N = N
        self.Edge = [[] for _ in range(N)]

    def add_edge(self, st, en, cap, cost):
        self.Edge[st].append([en, cap, cost, len(self.Edge[en])])
        self.Edge[en].append([st, 0, -cost, len(self.Edge[st]) - 1])

    def get_mf(self, so, si, fl):
        N = self.N
        INF = self.INF
        res = 0
        Pot = [0] * N
        geta = N
        prv = [None] * N
        prenum = [None] * N
        while fl:
            dist = [INF] * N
            dist[so] = 0
            Q = [so]
            while Q:
                (cost, vn) = divmod(hpp(Q), geta)
                if dist[vn] < cost:
                    continue
                for enum in range(len(self.Edge[vn])):
                    (vf, cap, cost, _) = self.Edge[vn][enum]
                    cc = dist[vn] + cost - Pot[vn] + Pot[vf]
                    if cap > 0 and dist[vf] > cc:
                        dist[vf] = cc
                        prv[vf] = vn
                        prenum[vf] = enum
                        hp(Q, cc * geta + vf)
            if dist[si] == INF:
                return -1
            for i in range(N):
                Pot[i] -= dist[i]
            cfl = fl
            vf = si
            while vf != so:
                cfl = min(cfl, self.Edge[prv[vf]][prenum[vf]][1])
                vf = prv[vf]
            fl -= cfl
            res -= cfl * Pot[si]
            vf = si
            while vf != so:
                e = self.Edge[prv[vf]][prenum[vf]]
                e[1] -= cfl
                self.Edge[vf][e[3]][1] += cfl
                vf = prv[vf]
        return res


N = int(readline())
(ra, sa, pa) = map(int, readline().split())
(rb, sb, pb) = map(int, readline().split())
maxwin = min(ra, sb) + min(sa, pb) + min(pa, rb)
D = MinCostFlowwithDijkstra(8)
D.add_edge(0, 1, ra, 0)
D.add_edge(0, 2, sa, 0)
D.add_edge(0, 3, pa, 0)
D.add_edge(4, 7, rb, 0)
D.add_edge(5, 7, sb, 0)
D.add_edge(6, 7, pb, 0)
D.add_edge(1, 4, N, 0)
D.add_edge(1, 5, N, 1)
D.add_edge(1, 6, N, 0)
D.add_edge(2, 4, N, 0)
D.add_edge(2, 5, N, 0)
D.add_edge(2, 6, N, 1)
D.add_edge(3, 4, N, 1)
D.add_edge(3, 5, N, 0)
D.add_edge(3, 6, N, 0)
print(D.get_mf(0, 7, N), maxwin)
