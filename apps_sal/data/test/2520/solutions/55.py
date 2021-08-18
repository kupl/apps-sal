n, m, k = map(int, input().split())


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


all1 = [0] * (n)

uf = UnionFind(n)
for i in range(m):
    a, b = map(int, input().split())
    uf.unite(a, b)
    a, b = a - 1, b - 1

    all1[a] += 1
    all1[b] += 1
ans = [uf.size(x) - 1 - all1[x - 1] for x in range(1, n + 1)]

for i in range(k):
    a, b = map(int, input().split())
    if uf.same(a, b):
        a, b = a - 1, b - 1
        ans[a] -= 1
        ans[b] -= 1
print(*ans)
