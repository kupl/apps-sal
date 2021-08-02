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

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def group_size(self, x):
        return self.size[self.find(x)]


n, m = map(int, input().split())
x = [0] * m
x[m - 1] = n * (n - 1) // 2
uf = UnionFind(n)
a = [0] * m
b = [0] * m
for i in range(m):
    a[i], b[i] = map(int, input().split())
    a[i] -= 1
    b[i] -= 1
for i in range(m - 1, 0, -1):
    if uf.is_same(a[i], b[i]):
        x[i - 1] = x[i]
    else:
        x[i - 1] = x[i] - uf.group_size(a[i]) * uf.group_size(b[i])
        uf.unite(a[i], b[i])
print(*x, sep="\n")
