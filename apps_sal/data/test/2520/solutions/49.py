class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n)
        self.rank = [0] * (n)

    def find_root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def same(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def count(self, x):
        return -self.root[self.find_root(x)]

    def members(self, x):
        root = self.find_root(x)
        return [i for i in range(self.n) if self.find_root(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}


N, M, K = map(int, input().rstrip().split())
AB = [list(map(int, input().rstrip().split()))for _ in range(M)]
CD = [list(map(int, input().rstrip().split()))for _ in range(K)]

u = UnionFind(N)
for a, b in AB:
    u.unite(a - 1, b - 1)

ans = [u.count(i) - 1 for i in range(N)]
ans

for a, b in AB:
    if u.same(a - 1, b - 1):
        ans[a - 1] -= 1
        ans[b - 1] -= 1

for c, d in CD:
    if u.same(c - 1, d - 1):
        ans[c - 1] -= 1
        ans[d - 1] -= 1
print(*ans)
