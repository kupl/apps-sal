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
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, self.members(r)) for r in self.roots()))


(n, m) = map(int, input().split())
ab = [0] * m
for i in range(m):
    ab[i] = list(map(int, input().split()))
ans = [0] * (m + 1)
ans[0] = n * (n - 1) // 2
uf = UnionFind(n + 1)
ab = ab[::-1]
for (i, [a, b]) in enumerate(ab):
    if uf.find(a) == uf.find(b):
        ans[i + 1] = ans[i]
    else:
        ans[i + 1] = ans[i] - uf.size(a) * uf.size(b)
    uf.union(a, b)
for i in range(m):
    print(ans[-i - 2])
