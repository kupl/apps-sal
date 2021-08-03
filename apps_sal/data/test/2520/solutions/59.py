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
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


n, m, k = map(int, input().split())
ans = [-1 for _ in range(n)]
UF = UnionFind(n)
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    UF.union(a, b)
    ans[a] -= 1
    ans[b] -= 1

for i in range(n):
    ans[i] += UF.size(i)

for _ in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if UF.same(c, d):
        ans[c] -= 1
        ans[d] -= 1
print(*ans)
