from collections import Counter


class Union_Find:

    def __init__(self, n):
        self.par = [-1] * n
        self.siz = [1] * n

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.siz[x] < self.siz[y]:
            tmp = x
            x = y
            y = tmp
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

    def size(self, x):
        return self.siz[self.root(x)]


(N, K, L) = map(int, input().split())
road_uf = Union_Find(N)
train_uf = Union_Find(N)
for _ in range(K):
    (p, q) = map(int, input().split())
    p -= 1
    q -= 1
    road_uf.unite(p, q)
for _ in range(L):
    (r, s) = map(int, input().split())
    r -= 1
    s -= 1
    train_uf.unite(r, s)
roots = [''] * N
for i in range(N):
    r = str(road_uf.root(i)) + '-' + str(train_uf.root(i))
    roots[i] = r
counts = Counter(roots)
ans = [1] * N
for i in range(N):
    r = roots[i]
    ans[i] = counts[r]
print(*ans)
