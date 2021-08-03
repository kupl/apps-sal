n, m = list(map(int, input().split()))
lrd = [tuple(map(int, input().split())) for i in range(m)]


class WeightedUnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.count = 0
        self.weight = [0] * n

    def root(self, a):
        if self.parent[a] == a:
            return a
        else:
            pa = self.root(self.parent[a])
            self.weight[a] += self.weight[self.parent[a]]
            self.parent[a] = pa
            return pa

    def is_same(self, a, b):
        return self.root(a) == self.root(b)

    def unite(self, a, b, w):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
            self.weight[ra] = w - self.weight[a] + self.weight[b]
        else:
            self.parent[rb] = ra
            self.weight[rb] = -w - self.weight[b] + self.weight[a]
            if self.rank[ra] == self.rank[rb]:
                self.rank[ra] += 1
        self.count += 1

    def diff(self, a, b):
        return self.weight[a] - self.weight[b]


uf = WeightedUnionFind(n)
for l, r, d in lrd:
    l, r = l - 1, r - 1
    if uf.is_same(l, r):
        if uf.diff(l, r) != d:
            print('No')
            return
    else:
        uf.unite(l, r, d)
print('Yes')
