from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * (n + 1)

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
        return [i for i in range(self.n + 1) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


N = int(input())
U = UnionFind(2 * 10**5)
for i in range(N):
    x, y = map(int, input().split())
    U.union(x, y + 10**5)
ans = 0
Roots = U.roots()
D = {x: [] for x in Roots}
for i in range(2 * 10**5 + 1):
    D[U.find(i)].append(i)
for x in Roots:
    ss = D[x]
    sx = 0
    sy = 0
    for c in ss:
        if c <= 10**5:
            sx += 1
        else:
            sy += 1
    ans += sx * sy
ans -= N
print(ans)
