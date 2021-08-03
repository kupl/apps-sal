class DisjointSet:
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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.parents[self.find(x)]


N, M, *ab = list(map(int, open(0).read().split()))
edges = [(a - 1, b - 1) for a, b in zip(*[iter(ab)] * 2)]

ans = 0
for i in range(M):
    ds = DisjointSet(N)
    for j in range(M):
        if i == j:
            continue
        ds.union(*edges[j])
    if len([-p for p in ds.parents if p < 0]) > 1:
        ans += 1
print(ans)
