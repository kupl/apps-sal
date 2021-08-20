class UnionFind(object):

    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        (x, y) = (self.find(x), self.find(y))
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


(N, M) = map(int, input().split())
uf = UnionFind(N)
for _ in range(M):
    (x, y, z) = map(int, input().split())
    uf.unite(x - 1, y - 1)
for i in range(N):
    uf.find(i - 1)
s = set(uf.parent)
print(len(s))
