# https://note.nkmk.me/python-union-find/
class UnionFind():
    def __init__(self, n):  # O(n == 頂点の個数)
        self.n = n
        self.parents = [-1] * n

    def find(self, x):  # O(xのグループのサイズ) 根のインデックスを返す ならし計算量O(α(頂点数))
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])  # 経路圧縮
            return self.parents[x]

    def union(self, x, y):  # O(xかyのグループのサイズ) xとyを連結する
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return x

    def size(self, x):  # O(xのグループのサイズ) xのグループのサイズ
        return -self.parents[self.find(x)]

    def same(self, x, y):  # O(xのグループサイズ) xとyが同じグループに属する(True)かどうか
        return self.find(x) == self.find(y)

    def members(self, x):  # O(頂点数) xと同じグループの頂点たちのリスト すべてのグループを使いたいならall_group_members
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):  # O(頂点数) 親のインデックスたちのリスト
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):  # O(頂点数) グループの個数
        return len(self.roots())

    def group_sizes(self):  # O(頂点数) すべてのグループのサイズのリスト
        return [uf.size(x) for x in uf.roots()]

    def all_group_members(self):  # O(頂点数 * xの連結成分サイズ)? グループたち(リスト)のリスト
        group = {r: [] for r in self.roots()}
        for i in range(self.n):
            group[self.find(i)].append(i)
        return list(group.values())

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


N, M = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
CD = [[int(i) for i in input().split()] for j in range(M)]

uf = UnionFind(N)
for c, d in CD:
    uf.union(c - 1, d - 1)

gr = uf.all_group_members()

for g in gr:
    asum = sum([A[i] for i in g])
    bsum = sum([B[i] for i in g])
    if asum != bsum:
        print("No")
        return

print("Yes")
