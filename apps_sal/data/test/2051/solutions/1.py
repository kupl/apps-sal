import collections


class UnionFind:

    def __init__(self, size):
        self.size = size
        self.table = [-1 for _ in range(size)]

    def find(self, x):
        while self.table[x] >= 0:
            if self.table[self.table[x]] >= 0:
                self.table[x] = self.table[self.table[x]]
            x = self.table[x]
        return x

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] >= self.table[s2]:
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
        return self.table[s1]

    def count_group(self):
        count = 0
        for i in range(self.size):
            if self.table[i] < 0:
                count += 1
        return count


(n, m, k) = map(int, input().split())
c = [0] + list(map(int, input().split()))
uf = UnionFind(n + 1)
use = [False] * (n + 1)
for i in range(m):
    (li, ri) = map(int, input().split())
    uf.union(li, ri)
    use[li] = True
    use[ri] = True
groups = {}
for i in range(1, n + 1):
    if not use[i]:
        continue
    g = uf.find(i)
    if g not in groups:
        groups.update({g: collections.defaultdict(int)})
    groups[g][c[i]] += 1
total = 0
for g in groups.values():
    total += sum(g.values()) - max(g.values())
print(total)
