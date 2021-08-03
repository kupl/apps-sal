class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]


N, M = list(map(int, input().split()))

uf = UnionFind(N)

for i in range(M):
    A, B = list(map(int, input().split()))
    a = uf.find(A - 1)
    b = uf.find(B - 1)
    uf.union(a, b)

ans = 0

for i in uf.roots():
    ans = max(uf.size(i), ans)

print(ans)
