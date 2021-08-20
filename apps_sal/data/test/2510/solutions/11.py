class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * (n + 1)

    def find(self, x):
        if self.parents[x] < 0:
            return x
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
        return -1 * self.parents[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i in range(1, self.n + 1, 1) if self.parents[i] < 0]

    def group_count(self):
        return len(self.roots())


(N, M) = map(int, input().split())
uf = UnionFind(N)
for i in range(M):
    (a, b) = map(int, input().split())
    uf.union(a, b)
ans = 0
for r in uf.roots():
    ans = max(ans, uf.size(r))
print(ans)
