class UnionFind:
    def __init__(self, size):
        self.data = [-1] * size

    def root(self, x):
        if self.data[x] < 0:
            return x
        ans = self.root(self.data[x])
        self.data[x] = ans
        return ans

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.data[x] > self.data[y]:
            x, y = y, x
        self.data[x] += self.data[y]
        self.data[y] = x
        return True

    def same(self, x, y):
        return self.root(x) == self.root(y)


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

uf = UnionFind(n)

for _ in range(m):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    uf.unite(c, d)

l = [0] * n

for i in range(n):
    p = uf.root(i)
    l[p] += a[i]
    l[p] -= b[i]

if all([x == 0 for x in l]):
    print('Yes')
else:
    print('No')
