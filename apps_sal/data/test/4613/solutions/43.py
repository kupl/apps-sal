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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return list(i for i in range(self.n) if self.find(i) == root)

    def roots(self):
        return list(i for i, x in enumerate(self.parents) if x < 0)

    def group_count(self):
        return len(self.roots)

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


adj = []
N, M = map(int, input().split())
for m in range(M):
    a, b = map(int, input().split())
    adj.append([a - 1, b - 1])

ans = 0
for i in range(M):
    uf = UnionFind(N)
    for j in range(M):
        if i == j:
            continue
        uf.union(*adj[j])
    if len(set(uf.roots())) != 1:
        ans += 1
print(ans)
