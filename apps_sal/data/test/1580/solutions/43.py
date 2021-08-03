class UnionFind:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.components = n

    def root(self, x):
        if self.p[x] == x:
            return x
        else:
            self.p[x] = self.root(self.p[x])
            return self.p[x]

    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x != y:
            self.p[x] = y
            self.components -= 1

    def same(self, x, y):
        return (self.root(x) == self.root(y))


N, M = map(int, input().split())

UF = UnionFind(N)

for _ in range(M):
    X, Y, Z = map(int, input().split())
    X, Y = X - 1, Y - 1
    UF.unite(X, Y)

print(UF.components)
