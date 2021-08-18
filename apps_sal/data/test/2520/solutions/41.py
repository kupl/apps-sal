import sys
sys.setrecursionlimit(100000)


class UnionFind:
    """
    子ノードには自分の親ノードIDを記録。親ノードにはグループサイズの負値を記録。
    """

    def __init__(self, n):
        self.node = [-1] * n

    def unite(self, x, y):
        """
        xとyが属するグループを統合
        """
        _x, _y = self.find(x), self.find(y)
        if _x == _y:
            return False
        if abs(self.node[_x]) < abs(self.node[_y]):
            self.node[_x], self.node[_y] = self.node[_y], self.node[_x]
        self.node[_x] += self.node[_y]
        self.node[_y] = _x
        return True

    def find(self, x):
        """
        xが属するグループの親ノードインデックスを検索。
        """
        _val = self.node[x]
        if _val < 0:
            return x
        self.node[x] = self.find(_val)
        return self.node[x]

    def same(self, x, y):
        """
        xとyが属するグループが同じかチェック。
        """
        return self.find(x) == self.find(y)

    def size(self, x):
        """
        xが属するグループの総サイズ取得
        """
        return abs(self.node[self.find(x)])

    def __str__(self):
        return str(self.node)


N, M, K = map(int, input().split())

uf = UnionFind(N)
friend = [0] * N
block = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    uf.unite(a, b)
    friend[a], friend[b] = friend[a] + 1, friend[b] + 1

for _ in range(K):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    block[c].append(d)
    block[d].append(c)

for i in range(N):
    ans = uf.size(i) - friend[i] - 1
    for j in block[i]:
        if uf.same(i, j):
            ans -= 1
    print("{} ".format(ans), end="")
print("")
