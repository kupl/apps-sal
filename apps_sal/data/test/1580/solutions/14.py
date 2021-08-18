n, m = map(int, input().split())


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * (n)
        self.size = [1] * (n)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def all_find(self):
        for n in range(len(self.par)):
            self.find(n)


uf = UnionFind(n)

for _ in range(m):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    uf.union(x, y)

root = set([])

for i in range(n):
    root.add(uf.find(i))

print(len(root))
