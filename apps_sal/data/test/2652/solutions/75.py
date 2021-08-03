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
xy = [list(map(int, input().split())) + [i] for i in range(n)]
"""
辺を結びたいがすべての点で結ぶと膨大になる
"""

edge = []
xy.sort()
for i, j in zip(list(range(n - 1)), list(range(1, n))):
    cost = xy[j][0] - xy[i][0]
    heapq.heappush(edge, [cost, xy[i][2], xy[j][2]])

xy.sort(key=lambda x: x[1])
for i, j in zip(list(range(n - 1)), list(range(1, n))):
    cost = xy[j][1] - xy[i][1]
    heapq.heappush(edge, [cost, xy[i][2], xy[j][2]])

uf = UnionFind(n)
ans = 0
while edge:
    c, a, b = heapq.heappop(edge)
    if uf.same(a, b):
        continue
    uf.union(a, b)
    ans += c

print(ans)
