I = [int(_) for _ in open(0).read().split()]
N, M = I[:2]
A = I[2:2 + N]
B = I[2 + N:2 + N + N]
CD = I[2 + N + N:]
C, D = [CD[_::len('CD')] for _ in range(len('CD'))]


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 0
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.root[self.find(x)]


uf = UnionFind(N)
for c, d in zip(C, D):
    uf.unite(c, d)
sums = [0] * (N + 1)
for i in range(1, N + 1):
    sums[uf.find(i)] += B[i - 1] - A[i - 1]
print(('Yes' if all(x == 0 for x in sums) else 'No'))

