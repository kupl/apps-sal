import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


class UnionFind:
    # 初期化
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        # 親要素のノード番号を格納する.初めは全て親ノード.
        # self.parent[x] == x の時，そのノードは根.
        self.parent = [i for i in range(n_nodes)]
        # 木の高さを格納する．
        self.rank = [1] * n_nodes
        # 自分と同じグループの要素数を格納．親要素を参照するようにする
        self.size = [1] * n_nodes

    # 検索. 根を返す.
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            # 一度調べた値は，根に繋ぎ直す.
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    # 併合.
    # 木の高さが低くなるように.
    # 親要素の書き換えは少ない方がいい
    def unite(self, x, y):
        # 根を探す．
        x = self.find(x)
        y = self.find(y)
        # 根が同じ場合はそのまま
        if x == y:
            return
        # 木の高さを比較し，低い方を高い方の根に貼る.
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.size[x] += self.size[y]
        else:
            self.parent[x] = y
            self.size[y] += self.size[x]
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    # 同じ集合に属するか判定
    def check(self, x, y):
        return self.find(x) == self.find(y)

    # 同一グループに所属する要素数を返す
    def get_size(self, x):
        return self.size[self.find(x)]

    # 親要素のリストを返す
    def get_parent_list(self):
        return [i for i in range(self.n_nodes) if self.find(i) == i]

    # グループの数を返す
    def get_n_groups(self):
        return len(self.get_parent_list())

    # 同じグループに所属する要素の集合を返す
    def get_members(self, x):
        parent = self.find(x)
        return [i for i in range(self.n_nodes) if self.find(i) == parent]

    # 全ての根に対する，グループのメンバーを返す．
    def get_members_dict(self):
        return {par: self.get_members(par) for par in self.get_parent_list()}


def main():
    N, M = list(map(int, input().split()))
    edge = [set(map(int, input().split())) for _ in range(M)]

    UF = UnionFind(N)
    for x, y in edge:
        UF.unite(x - 1, y - 1)

    parents = UF.get_parent_list()
    answer = 0
    for p in parents:
        size = UF.get_size(p)
        answer = max(answer, size)
    print(answer)


def __starting_point():
    main()

__starting_point()
