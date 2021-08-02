class UnionFind:

    def __init__(self, n):
        self.par = [-1] * n

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.par[x] > self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x
        return True

    def root(self, x):
        path = []
        while self.par[x] >= 0:
            path.append(x)
            x = self.par[x]
        for y in path:
            self.par[y] = x
        return x

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.par[self.root(x)]


n, m = map(int, input().split())
uni = UnionFind(n)
for _ in range(m):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    uni.unite(x, y)

a = [0] * n
for i in range(n):
    a[uni.root(i)] = 1

print(sum(a))
