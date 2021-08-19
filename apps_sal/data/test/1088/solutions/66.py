import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 998244353


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        """xの親を返す"""
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """yをxの根に繋ぐ（マージテク有）"""
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        """xとyが同じ連結成分か判別する"""
        return self.find(x) == self.find(y)

    def size(self, x):
        """xの連結成分の大きさを返す"""
        return -self.parents[self.find(x)]

    def kruskal(self, edge):
        """
        :param edge: edge = [(コスト, 頂点1, 頂点2),...]の形で重み付き隣接リストを渡して下さい
        :return: 最小全域木のコストの和
        """
        edge.sort()
        cost_sum = 0
        for (cost, node1, node2) in edge:
            if not self.same(node1, node2):
                cost_sum += cost
                self.union(node1, node2)
        return cost_sum


def resolve():
    (n, k) = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(n)]
    uf_row = UnionFind(n)
    for x in range(n):
        for y in range(x + 1, n):
            for i in range(n):
                if A[x][i] + A[y][i] > k:
                    break
            else:
                uf_row.union(x, y)
    uf_col = UnionFind(n)
    for x in range(n):
        for y in range(x + 1, n):
            for i in range(n):
                if A[i][x] + A[i][y] > k:
                    break
            else:
                uf_col.union(x, y)
    fact = [1, 1]
    for i in range(2, n + 1):
        fact.append(fact[-1] * i % mod)
    size_row = [1] * n
    for i in range(n):
        root = uf_row.find(i)
        size_row[root] = uf_row.size(root)
    size_col = [1] * n
    for i in range(n):
        root = uf_col.find(i)
        size_col[root] = uf_col.size(root)
    tot_row = tot_col = 1
    for (i, j) in zip(size_row, size_col):
        tot_row = tot_row * fact[i] % mod
        tot_col = tot_col * fact[j] % mod
    res = tot_row * tot_col % mod
    print(res)


def __starting_point():
    resolve()


__starting_point()
