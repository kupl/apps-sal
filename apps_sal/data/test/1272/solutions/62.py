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

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.parents[self.find(x)]


N, M = map(int, input().split())
inconvenience = N * (N - 1) // 2
score = []
UF = UnionFind(N)
A = [0] * M
for i in range(M):
    a, b = map(int, input().split())
    A[i] = [a - 1, b - 1]
for a, b in A[::-1]:
    score.append(inconvenience)
    if not UF.same(a, b):
        inconvenience -= UF.size(a) * UF.size(b)
    UF.unite(a, b)
for s in score[::-1]:
    print(s)
