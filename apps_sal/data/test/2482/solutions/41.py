from collections import Counter


class UnionFind:

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
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return abs(self.parents[self.find(x)])


(N, K, L) = list(map(int, input().split()))
uf_road = UnionFind(N + 1)
uf_train = UnionFind(N + 1)
road_dict = dict()
train_dict = dict()
for _ in range(K):
    (p, q) = list(map(int, input().split()))
    uf_road.union(p, q)
for _ in range(L):
    (r, s) = list(map(int, input().split()))
    uf_train.union(r, s)
set_id_pairs = [(uf_road.find(i), uf_train.find(i)) for i in range(1, N + 1)]
counter = Counter(set_id_pairs)
counts = [counter[set_id_pairs[i]] for i in range(N)]
print(' '.join((str(c) for c in counts)))
