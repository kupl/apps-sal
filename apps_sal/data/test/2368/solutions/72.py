class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1

    def group_members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parent) if i == x]

    def all_group_members(self):
        return {r: self.group_members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.group_members(r)) for r in self.roots())


n, m = list(map(int, input().split()))
uf = UnionFind(n)
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

for _ in range(m):
    c, d = [int(x) - 1 for x in input().split()]
    uf.unite(c, d)

asum = [0] * n
bsum = [0] * n

for i in range(n):
    root = uf.find(i)
    asum[root] += al[i]
    bsum[root] += bl[i]

if asum == bsum:
    print('Yes')
else:
    print('No')
