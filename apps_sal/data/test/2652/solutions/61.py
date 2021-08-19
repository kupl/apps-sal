import sys
input = sys.stdin.readline
N = int(input())
d = []
for i in range(N):
    (x, y) = list(map(int, input().split()))
    d.append((i + 1, x, y))
edge = []
d.sort(key=lambda x: x[1])
for i in range(N - 1):
    (a, px, py) = d[i]
    (b, qx, qy) = d[i + 1]
    dis = abs(px - qx)
    edge.append((dis, a, b))
    edge.append((dis, b, a))
d.sort(key=lambda x: x[2])
for i in range(N - 1):
    (a, px, py) = d[i]
    (b, qx, qy) = d[i + 1]
    dis = abs(py - qy)
    edge.append((dis, a, b))
    edge.append((dis, b, a))


class UnionFind:

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
            (x, y) = (y, x)
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
        return [i for (i, x) in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, self.members(r)) for r in self.roots()))


edge.sort()


def kruskal():
    res = 0
    G = UnionFind(N)
    for (cost, p, q) in edge:
        if not G.same(p, q):
            G.union(p, q)
            res += cost
    return res


ans = kruskal()
print(ans)
