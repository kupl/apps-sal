class UnionFind:
    def __init__(self, n):
        self.ps = [-1] * (n + 1)

    def find(self, x):
        if self.ps[x] < 0:
            return x
        else:
            self.ps[x] = self.find(self.ps[x])
            return self.ps[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.ps[x] > self.ps[y]:
            x, y = y, x
        self.ps[x] += self.ps[y]
        self.ps[y] = x
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        x = self.find(x)
        return -self.ps[x]


n = int(input())
v = 10**5 + 5
uf = UnionFind(v * 2 + 10)
for _ in range(n):
    x, y = map(int, input().split())
    uf.unite(x, y + v)
d = dict()
for i in range(v * 2):
    if uf.size(i) > 1:
        p = uf.find(i)
        if p not in d:
            d[p] = [0, 0]
        d[p][i > v] += 1
print(sum(x * y for x, y in d.values()) - n)
