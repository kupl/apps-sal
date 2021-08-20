from collections import Counter
(n, k, l) = map(int, input().split())


class UnionFind(object):

    def __init__(self, n):
        self._par = list(range(n))
        self.size = [1] * n

    def root(self, v):
        if self._par[v] == v:
            return v
        self._par[v] = self.root(self._par[v])
        return self._par[v]

    def unite(self, u, v):
        (u, v) = (self.root(u), self.root(v))
        if u == v:
            return False
        if self.size[u] > self.size[v]:
            (u, v) = (v, u)
        self.size[v] += self.size[u]
        self._par[u] = v

    def is_connected(self, u, v):
        return self.root(u) == self.root(v)


rood = UnionFind(n)
train = UnionFind(n)
for _ in range(k):
    (p, q) = map(int, input().split())
    rood.unite(p - 1, q - 1)
for _ in range(l):
    (r, s) = map(int, input().split())
    train.unite(r - 1, s - 1)
cnt = Counter()
for i in range(n):
    (root_r, root_t) = (rood.root(i), train.root(i))
    cnt[root_r, root_t] += 1
ans = []
for i in range(n):
    (root_r, root_t) = (rood.root(i), train.root(i))
    ans.append(cnt[root_r, root_t])
print(*ans)
