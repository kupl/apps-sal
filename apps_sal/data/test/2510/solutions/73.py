class union_find():

    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find_root(self, x):
        if self.root[x] < 0:
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
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def same(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def cnt(self, x):
        return -self.root[self.find_root(x)]


n, m = map(int, input().split())
g = union_find(n)
ans = 0
for _ in range(m):
    a, b = map(int, input().split())
    g.unite(a, b)

for i in range(1, n+1):
    ans = max(ans, g.cnt(i))

print(ans)
