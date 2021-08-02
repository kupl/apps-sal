class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(self.n)]
        self.rank = [0] * self.n

    def find_root(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find_root(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        rx = self.find_root(x)
        ry = self.find_root(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        else:
            self.parent[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def is_same(self, x, y):
        return self.find_root(x) == self.find_root(y)


N, M = map(int, input().split())
edge = []
bridge = 0
for _ in range(M):
    e = list(map(lambda x: int(x) - 1, input().split()))
    edge.append(e)

for i in range(M):
    uf = UnionFind(N)
    for j in range(M):
        if j == i:
            continue
        uf.unite(edge[j][0], edge[j][1])
    if uf.find_root(edge[i][0]) != uf.find_root(edge[i][1]):
        bridge += 1

print(bridge)
