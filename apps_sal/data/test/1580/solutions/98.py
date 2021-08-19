import sys
readline = sys.stdin.readline

N, M = list(map(int, readline().split()))

# by size
# 0-indexed


class UnionFind:
    N = 0
    parent = None
    size = None

    def __init__(self, N):
        self.N = N
        self.parent = [i for i in range(self.N)]
        self.size = [1] * self.N

    def root(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.size[x] > self.size[y]:
            # 大きい方にくっつける
            self.parent[y] = x
            self.size[x] += self.size[y]
        else:
            self.parent[x] = y
            self.size[y] += self.size[x]

    def get_group_size(self, x):
        return self.size[self.root(x)]

    def get_roots(self):
        r = set()
        for i in range(self.N):
            r.add(self.root(i))
        return r

    def show_parent(self):
        print((self.parent))

    def show_size(self):
        print((self.size))


UF = UnionFind(N)

for i in range(M):
    x, y, z = list(map(int, readline().split()))
    UF.unite(x - 1, y - 1)

print((len(UF.get_roots())))
