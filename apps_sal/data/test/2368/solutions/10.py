from collections import defaultdict


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


uf = UnionFind(6)
(n, m) = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dic = {}
flag = True
for i in range(n):
    dic.setdefault(i, B[i] - A[i])
uf = UnionFind(n)
for _ in range(m):
    (c, d) = map(int, input().split())
    (c, d) = (c - 1, d - 1)
    uf.union(c, d)
for gr in uf.all_group_members().values():
    tem = 0
    for point in gr:
        tem += dic[point]
    if not tem == 0:
        flag = False
if flag:
    print('Yes')
else:
    print('No')
