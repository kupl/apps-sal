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


n, m, k = map(int, input().split())
a = [0] * m
b = [0] * m
c = [0] * k
d = [0] * k
x = [0] * n
direct = [[] for _ in range(n)]
uf = UnionFind(n)
for i in range(m):
    a[i], b[i] = map(int, input().split())
    a[i] -= 1
    b[i] -= 1
    direct[a[i]].append(b[i])
    direct[b[i]].append(a[i])
    uf.unite(a[i], b[i])
for i in range(k):
    c[i], d[i] = map(int, input().split())
    c[i] -= 1
    d[i] -= 1
    if uf.is_same(c[i], d[i]):
        direct[c[i]].append(d[i])
        direct[d[i]].append(c[i])
for i in range(n):
    x[i] = uf.group_size(i) - len(direct[i]) - 1
print(*x)
