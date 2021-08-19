class BellmanFord:
    """ベルマンフォード法で最短経路を求める"""

    def __init__(self, s, V):
        """
        Args:
            s(int): 始点
            V(int): 頂点数
        """
        self.graph = {}
        for i in range(V):
            self.graph[i] = []
        self._V = V
        self.dst = [float('inf') for _ in range(V)]
        self.dst[s] = 0

    @property
    def dist(self):
        return self.dst

    @property
    def V(self):
        return self._V

    def add(self, a, b, cost):
        """頂点aから頂点bへのコストはcost"""
        self.graph[a].append((b, cost))

    def shortest_path(self):
        """始点sからの最短経路を求める
        Returns:
            (bool): 負の閉路が存在する(True) / 存在しない(False)
        """
        for t in range(self.V):
            update = False
            for u in range(self.V):
                if self.dst[u] == float('inf'):
                    continue
                for (v, cost) in self.graph[u]:
                    if self.dst[v] > self.dst[u] + cost:
                        self.dst[v] = self.dst[u] + cost
                        update = True
                        if t == self.V - 1 and v == self.V - 1:
                            return True
            if not update:
                break
        return False


def solve():
    (N, M) = list(map(int, input().split()))
    bf = BellmanFord(0, N)
    for _ in range(M):
        (a, b, c) = list(map(int, input().split()))
        bf.add(a - 1, b - 1, -c)
    nloop = bf.shortest_path()
    if nloop:
        print('inf')
    else:
        print(-bf.dist[N - 1])


def __starting_point():
    solve()


__starting_point()
