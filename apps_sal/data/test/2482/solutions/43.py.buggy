from collections import Counter


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.group_count = n

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

        self.group_count -= 1

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

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}


def int_(num_str):
    return int(num_str) - 1


N, K, L = list(map(int, input().split()))
uf1 = UnionFind(N)
for _ in range(K):
    p, q = list(map(int_, input().split()))
    uf1.union(p, q)
uf2 = UnionFind(N)
for _ in range(L):
    r, s = list(map(int_, input().split()))
    uf2.union(r, s)
pair = [(uf1.find(i), uf2.find(i)) for i in range(N)]
ans = Counter(pair)
print((*[ans[p] for p in pair]))
