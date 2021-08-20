class UnionFind:

    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)

    def find(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.root[x] > self.root[y]:
            (x, y) = (y, x)
        self.root[x] += self.root[y]
        self.root[y] = x

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.root[self.find(x)]


(n, m, k) = map(int, input().split())
friends = UnionFind(n)
f_or_b = [1] * (n + 1)
for i in range(m):
    (a, b) = map(int, input().split())
    friends.unite(a, b)
    f_or_b[a] += 1
    f_or_b[b] += 1
for i in range(k):
    (c, d) = map(int, input().split())
    if friends.is_same(c, d):
        f_or_b[c] += 1
        f_or_b[d] += 1
print(*[friends.size(i) - f_or_b[i] for i in range(1, n + 1)])
