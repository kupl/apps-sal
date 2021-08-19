from collections import defaultdict


def Yes_No(flag):
    if flag:
        print('Yes')
    else:
        print('No')


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for (i, x) in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join((f'{r}: {m}' for (r, m) in self.all_group_members().items()))


(n, m) = list(map(int, input().split()))
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))
cds = [list(map(int, input().split())) for _ in range(m)]
uf = UnionFind(n)
for i in range(m):
    (x, y) = cds[i]
    uf.union(x - 1, y - 1)
ans = True
for (key, val) in uf.all_group_members().items():
    if sum((aa[i] for i in val)) != sum((bb[i] for i in val)):
        ans = False
Yes_No(ans)
