from collections import Counter
N, K, L = list(map(int, input().split()))


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find_root(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find_root(self.parents[x])
            return self.parents[x]

    def union_merge(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def union_size(self, x):
        return -self.parents[self.find_root(x)]

    def is_same_union(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def same_union_members(self, x):
        root = self.find_root(x)
        return [i for i in range(self.n) if self.find_root(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def union_count(self):
        return len(self.roots())

    def all_unions(self):
        return [self.same_union_members(r) for r in self.roots()]


road = UnionFind(N)
rail = UnionFind(N)

for i in range(K):
    p, k = list(map(int, input().split()))
    road.union_merge(p - 1, k - 1)

for i in range(L):
    r, s = list(map(int, input().split()))
    rail.union_merge(r - 1, s - 1)

root_combinations = []
for i in range(N):
    root_combinations.append((road.find_root(i), rail.find_root(i)))

same_combinations = Counter(root_combinations)
result = [same_combinations[root_combination] for root_combination in root_combinations]

ans = ' '.join(map(str, result))
print(ans)
