class ReRooting(object):
    """ 全方位木DP """

    def merge(self, a, b):
        """ 二項演算 a・b """
        return a * b % MOD

    def adj_bu(self, accBU, v: int):
        """
        Bottom-Upの単項演算 g(accBU[v])

        v: 頂点
        """
        return accBU * inv(self.SIZE[v]) % MOD

    def adj_td(self, accTD, v: int, p: int):
        """
        Top-Downの単項演算 g(accTD[v])

        v: 頂点
        p: 親
        """
        return accTD * inv(self.V - self.SIZE[v]) % MOD

    def adj_fin(self, acc, v: int):
        """
        最終結果の単項演算 g(acc[v])

        v: 頂点
        """
        return acc * fact[self.V - 1] % MOD

    def __init__(self, V: int, e: int):
        """
        V: 頂点数
        e: 単位元
        """
        self.V, self.e = V, e
        self.edge = [[] for _ in range(V)]
        self.par = [-1] * V
        self.order = []
        self.SIZE = [1] * self.V

    def subtree_size(self):
        """ 部分木のサイズを求める """
        for v in reversed(self.order[1:]):
            self.SIZE[self.par[v]] += self.SIZE[v]

    def add_edge(self, u: int, v: int):
        """ 辺(u,v)をグラフに追加する """
        self.edge[u].append(v)
        self.edge[v].append(u)

    def topological_sort(self, root: int = 0):
        """ トポロジカルソート """
        from collections import deque
        que = deque([root])
        while que:
            v = que.popleft()
            self.order.append(v)
            for w in self.edge[v]:
                if w != self.par[v]:
                    self.par[w] = v
                    que.append(w)

    def bottom_up(self):
        """ Bottom-Up DP """
        root = self.order[0]
        accBU = [self.e] * self.V
        resBU = [self.e] * self.V

        for v in reversed(self.order):
            resBU[v] = self.adj_bu(accBU[v], v)

            if v == root:
                break

            p = self.par[v]
            accBU[p] = self.merge(accBU[p], resBU[v])

        return accBU, resBU

    def top_down(self, resBU: list):
        """ Top-Down DP """
        accTD = [self.e] * self.V
        resTD = [self.e] * self.V

        for p in self.order:
            ac = resTD[p]
            for v in self.edge[p]:
                if v == self.par[p]:
                    continue
                accTD[v] = ac
                ac = self.merge(ac, resBU[v])

            ac = self.e
            for v in reversed(self.edge[p]):
                if v == self.par[p]:
                    continue
                accTD[v] = self.merge(accTD[v], ac)
                ac = self.merge(ac, resBU[v])
                resTD[v] = self.adj_td(accTD[v], v, p)

        return resTD

    def solve(self):
        self.topological_sort()
        self.subtree_size()
        accBU, resBU = self.bottom_up()
        resTD = self.top_down(resBU)
        res = [self.adj_fin(self.merge(a, b), v) for v, (a, b) in enumerate(zip(accBU, resTD))]
        return res


#########################################################################################
N = int(input())
MOD = 10 ** 9 + 7

fact = [1] * (N + 1)  # fact[n]: n!
factinv = [1] * (N + 1)  # n!の逆元
for i in range(N):
    fact[i + 1] = fact[i] * (i + 1) % MOD
factinv[-1] = pow(fact[-1], MOD - 2, MOD)
for i in range(N - 1, -1, -1):
    factinv[i] = factinv[i + 1] * (i + 1) % MOD


def inv(n): return fact[n - 1] * factinv[n] % MOD  # inv[n]: nの逆元


def main():
    RR = ReRooting(N, 1)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        RR.add_edge(a - 1, b - 1)

    print(*RR.solve(), sep="\n")


def __starting_point():
    main()


__starting_point()
