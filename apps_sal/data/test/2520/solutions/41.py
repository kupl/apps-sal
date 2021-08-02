import sys
# 再帰回数上弦を100000回に設定
sys.setrecursionlimit(100000)
# スタックサイズを無制限に設定
# resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))


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
        # xとyの親ノードインデックスを取得
        _x, _y = self.find(x), self.find(y)
        # 一致していれば同じグループに属しているので処理終了。
        # Falseはなぞ。
        if _x == _y:
            return False
        # サイズが小さいグループを大きいグループに結合するので、
        # _y側の絶対値がかならず小さくなるように前処理。(_yを_xのグループへ統合)
        # 大きい方を小さい方へ結合してしまうとノードが深くなってしまうので、
        # 計算量を削減するためのテクニック。
        if abs(self.node[_x]) < abs(self.node[_y]):
            self.node[_x], self.node[_y] = self.node[_y], self.node[_x]
        # グループサイズ更新
        self.node[_x] += self.node[_y]
        # _yの親ノードを_xに更新
        self.node[_y] = _x
        return True

    def find(self, x):
        """
        xが属するグループの親ノードインデックスを検索。
        """
        _val = self.node[x]
        # 負なら親ノードとみなして、そのインデックスを返す。
        if _val < 0:
            return x
        # グループの親ノードを再帰的に検索。
        # さらに、グループの親ノードIDを子ノードに記録しておくことで
        # 経路縮小を実現。
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
