from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):  # グループの根
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):  # xとyを併合
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):  # xが属するグループのサイズ数
        return -self.parents[self.find(x)]

    def same(self, x, y):  # xとyが同じグループか判定
        return self.find(x) == self.find(y)

    def members(self, x):  # xが属するグループのリスト
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):  # 全ての根のリスト
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):  # グループの数
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


N, M = map(int, input().split())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
uf = UnionFind(N)
for i in range(M):
    C, D = map(int, input().split())
    uf.union(C - 1, D - 1)
a = [0] * N
b = [0] * N
for i in range(N):
    a[uf.find(i)] += alist[i]
    b[uf.find(i)] += blist[i]
if a == b:
    print("Yes")
else:
    print("No")
