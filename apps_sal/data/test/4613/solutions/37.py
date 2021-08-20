class UnionFind:

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
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]


(n, m) = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
ans = 0
for i in range(m):
    uf = UnionFind(n)
    for j in range(m):
        if i != j:
            uf.union(a[j][0] - 1, a[j][1] - 1)
    if uf.size(0) != n:
        ans += 1
print(ans)
