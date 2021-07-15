class UnionFind:
    def __init__(self, n=0):
        self.d = [-1]*n
    def find(self, x):
        if self.d[x] < 0:
            return x
        else:
            self.d[x] = self.find(self.d[x])
            return self.d[x]
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.d[x] > self.d[y]:
            x, y = y, x
        self.d[x] += self.d[y]
        self.d[y] = x
        return True
    def same(self, x, y):
        return self.find(x) == self.find(y)
    def size(self, x):
        return -self.d[self.find(x)]

n, m, k = map(int, input().split())

deg = [0]*100005
uf = UnionFind(n)
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    deg[a] += 1
    deg[b] += 1
    uf.unite(a, b)
for _ in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if uf.same(c, d):
        deg[c] += 1
        deg[d] += 1
for i in range(n):
    print(uf.size(i) - 1 - deg[i], end="")
    if i == n-1:
        print()
    else:
        print(" ", end="")

