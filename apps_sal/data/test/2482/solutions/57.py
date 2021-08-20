from collections import Counter


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]


(n, k, l) = map(int, input().split())
pq = [list(map(int, input().split())) for i in range(k)]
rs = [list(map(int, input().split())) for i in range(l)]
uf_pq = UnionFind(n)
uf_rs = UnionFind(n)
for p in pq:
    (x, y) = p
    uf_pq.unite(x - 1, y - 1)
for r in rs:
    (x, y) = r
    uf_rs.unite(x - 1, y - 1)
pairs = []
for i in range(n):
    pairs.append((uf_pq.find(i), uf_rs.find(i)))
count = Counter(pairs)
ans = [count[pair] for pair in pairs]
print(*ans)
