from collections import Counter


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)
        self.rnk = [0] * (n + 1)

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
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1

    def isSame(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def size(self, x):
        return -self.root[self.find_root(x)]


(n, k, l) = map(int, input().split())
fe = UnionFind(n)
bus = UnionFind(n)
for _ in range(k):
    (p, q) = map(int, input().split())
    fe.unite(p, q)
for _ in range(l):
    (r, s) = map(int, input().split())
    bus.unite(r, s)
cnt = Counter()
for i in range(1, n + 1):
    cnt[fe.find_root(i), bus.find_root(i)] += 1
print(*[cnt[fe.find_root(i), bus.find_root(i)] for i in range(1, n + 1)])
