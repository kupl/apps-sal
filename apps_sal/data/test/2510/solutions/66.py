from collections import Counter


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [i for i in range(n + 1)]

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 0
        elif x < y:
            self.parents[y] = x
        else:
            self.parents[x] = y
        return 1


(n, m) = list(map(int, input().split()))
uf = UnionFind(n)
for _ in range(m):
    (a, b) = list(map(int, input().split()))
    uf.unite(a, b)
roots = []
for num in uf.parents:
    roots.append(uf.find(num))
count_roots = Counter(roots)
print(max(count_roots.values()))
