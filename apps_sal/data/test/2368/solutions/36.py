from collections import defaultdict

# n個の要素を0 ~ n - 1の番号で管理する。


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        # 各要素の親要素の番号を格納するリスト
        # 要素が根（ルート）の場合は-(そのグループの要素数)を格納する

    def find(self, x):
        # 要素xが属するグループの根を返す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        # 要素xが属するグループと要素yが属するグループとを併合する
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        # 要素xが属するグループのサイズ（要素数）を返す
        return -self.parents[self.find(x)]

    def same(self, x, y):
        #要素x, yが同じグループに属するかどうかを返す
        return self.find(x) == self.find(y)

    def members(self, x):
        # 要素xが属するグループに属する要素をリストで返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        # すべての根の要素をリストで返す
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        # グループの数を返す
        return len(self.roots())

    def all_group_members(self):
        # {ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
        # defaultdictは辞書dictのサブクラス
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        # print()での表示用
        # ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
        # f文字列を利用している
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
uf = UnionFind(n)
for i in range(m):
    x, y = map(int, input().split())
    uf.union(x - 1, y - 1)  # 0 ~ n - 1の番号で管理しているので、1-indexから0-indexに変更する。

# print(uf.roots())
# print(uf.group_count)
# print(uf.all_group_members())
# print(uf.all_group_members().values())
for i in (uf.all_group_members().values()):
    # print(i)
    c = 0
    d = 0
    for j in i:
        c += a[j]
        d += b[j]
    if c != d:
        print("No")
        break
else:
    # elseの中の処理は、for文の中のすべての処理が終わった後に実行されます。
    # breakが実行された場合は表示されません。
    print("Yes")
