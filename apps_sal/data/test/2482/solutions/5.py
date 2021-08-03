from collections import Counter


class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x

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


N, K, L = map(int, input().split())
uf_road = UnionFind(N + 1)
uf_train = UnionFind(N + 1)

for _ in range(K):
    p, q = map(int, input().split())
    uf_road.union(p, q)

for _ in range(L):
    s, t = map(int, input().split())
    uf_train.union(s, t)

union_sets = [(uf_road.find(i), uf_train.find(i)) for i in range(1, N + 1)]
counts = Counter(union_sets)
ans = [counts[union_set] for union_set in union_sets]

print(' '.join(str(a) for a in ans))
