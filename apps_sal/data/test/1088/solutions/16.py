import itertools
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


(N, K) = map(int, input().split())
l = [list(map(int, input().split())) for i in range(N)]
a = UnionFind(N)
for v in itertools.combinations(range(N), 2):
    for i in range(N):
        if l[i][v[0]] + l[i][v[1]] > K:
            break
        if i == N - 1:
            a.union(v[0], v[1])
b = UnionFind(N)
for v in itertools.combinations(range(N), 2):
    for i in range(N):
        if l[v[0]][i] + l[v[1]][i] > K:
            break
        if i == N - 1:
            b.union(v[0], v[1])
ans = 1
for x in a.roots():
    for i in range(1, a.size(x) + 1):
        ans = ans * i % 998244353
for x in b.roots():
    for i in range(1, b.size(x) + 1):
        ans = ans * i % 998244353
print(ans)
