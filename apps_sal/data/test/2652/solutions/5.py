import heapq


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

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
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


n = int(input())
a = []
b = []
for i in range(n):
    x, y = map(int, input().split())
    a.append((x, y, i))
    b.append((y, x, i))
a.sort()
b.sort()
edgea = []
edgeb = []
for i in range(n - 1):
    edgea.append((a[i + 1][0] - a[i][0], a[i][2], a[i + 1][2]))
    edgeb.append((b[i + 1][0] - b[i][0], b[i][2], b[i + 1][2]))
edge = edgea + edgeb
heapq.heapify(edge)

uf = UnionFind(n)
ans = 0
while len(edge):
    x, y, z = heapq.heappop(edge)
    if not uf.same(y, z):
        ans += x
        uf.union(y, z)
print(ans)
