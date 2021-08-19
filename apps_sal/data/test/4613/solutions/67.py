from collections import deque, defaultdict
import sys
sys.setrecursionlimit(2 ** 20)


class LowLink:
    """
    与えられたグラフの関節点と橋を求める
    Attributes:
    size:グラフの頂点
    pre:oreorderでの訪問順
    low: ###1. prenum[u]
         ###2.GのBackEdge(u,v)が存在する場合prenum[v]
         ###3.uをすべての子childに対してlowest[child]
    """

    def __init__(self, v):
        self.size = len(v) + 1
        self.v = v
        self.pre = [None] * self.size
        self.low = [None] * self.size
        self.articulations = []
        self.bridges = []
        for x in range(self.size):
            if self.pre[x] is None:
                self.cnt = 0
                self.dfs(x, None)

    def dfs(self, x, prev):
        self.pre[x] = self.low[x] = self.cnt
        self.cnt += 1
        is_articulation = False
        n = 0
        for y in self.v[x]:
            if self.pre[y] is None:
                n += 1
                low_y = self.dfs(y, x)
                if low_y < self.low[x]:
                    self.low[x] = low_y
                if self.pre[x] <= low_y:
                    if self.pre[x]:
                        is_articulation = True
                    if self.pre[x] < low_y:
                        self.bridges.append((min(x, y), max(x, y)))
            elif y != prev and self.pre[y] < self.low[x]:
                self.low[x] = self.pre[y]
        if prev is None and n > 1:
            is_articulation = True
        if is_articulation:
            self.articulations.append(x)
        return self.low[x]


def solve():
    (V, E) = map(int, input().split())
    G = defaultdict(lambda: [])
    for _ in range(E):
        (s, t) = map(int, input().split())
        G[s].append(t)
        G[t].append(s)
    lowlink = LowLink(G)
    bridges = lowlink.bridges
    print(len(bridges))


def __starting_point():
    solve()


__starting_point()
