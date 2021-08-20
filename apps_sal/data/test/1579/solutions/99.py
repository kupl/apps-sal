class UnionFind:

    def __init__(self, size):
        self.table = [-1] * size

    def root(self, x):
        while self.table[x] >= 0:
            x = self.table[x]
        return x

    def unite(self, x, y):
        s1 = self.root(x)
        s2 = self.root(y)
        if s1 != s2:
            if self.table[s1] > self.table[s2]:
                (s1, s2) = (s2, s1)
            self.table[s1] += self.table[s2]
            self.table[s2] = s1
        return

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.table[self.root(x)]


(n, *z) = map(int, open(0).read().split())
u = UnionFind(10 ** 5 * 2 + 1)
for (x, y) in zip(*[iter(z)] * 2):
    u.unite(x, 10 ** 5 + y)
d = [[0, set(), set()] for _ in range(10 ** 5 * 2 + 1)]
for (x, y) in zip(*[iter(z)] * 2):
    t = d[u.root(x)]
    t[0] += 1
    t[1].add(x)
    t[2].add(y)
print(sum((len(x) * len(y) - a for (a, x, y) in d)))
