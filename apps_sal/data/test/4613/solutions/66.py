class UnionFind:

    def __init__(self, n):
        self.n = n
        self.root = [-1] * n
        self.rnk = [0] * n

    def findRoot(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.findRoot(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.findRoot(x)
        y = self.findRoot(y)
        if x == y:
            return
        elif self.rnk[x] > self.rnk[y]:
            self.root[y] = x
        else:
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1

    def isSame(self, x, y):
        return self.findRoot(x) == self.findRoot(y)


(N, M) = map(int, input().split())
edge = [tuple(map(int, input().split())) for _ in range(M)]
cnt = 0
for i in range(M):
    uf = UnionFind(N + 1)
    for j in range(M):
        if j != i:
            uf.unite(edge[j][0], edge[j][1])
    if not uf.isSame(edge[i][0], edge[i][1]):
        cnt += 1
print(cnt)
