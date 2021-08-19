class UnionFind:

    def __init__(self, n):
        self.nodes = n
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n
        self.rank = [0] * n

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.sizes[y] += self.sizes[x]
                self.parents[x] = y
            else:
                self.sizes[x] += self.sizes[y]
                self.parents[y] = x
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def get_parents(self):
        for n in range(self.nodes):
            self.find(n)
        return self.parents


adj = []
(N, M) = map(int, input().split())
for m in range(M):
    (a, b) = map(int, input().split())
    adj.append([a - 1, b - 1])
ans = 0
for i in range(M):
    uf = UnionFind(N)
    for j in range(M):
        if i == j:
            continue
        uf.unite(*adj[j])
    if len(set(uf.get_parents())) != 1:
        ans += 1
print(ans)
