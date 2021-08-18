import sys
input = sys.stdin.readline


class UnionFind(object):
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


def __starting_point():
    N = int(input())
    vs = []
    for i in range(N):
        x, y = map(int, input().split())
        vs.append((x, y, i))
    vs.sort()
    edges = []
    for k in range(1, N):
        x, y, i = vs[k]
        a, b, j = vs[k - 1]
        edges.append((i, j, min(abs(x - a), abs(y - b))))
    vs.sort(key=lambda x: x[1])
    for k in range(1, N):
        x, y, i = vs[k]
        a, b, j = vs[k - 1]
        edges.append((i, j, min(abs(x - a), abs(y - b))))
    uf = UnionFind(N)
    edges.sort(key=lambda x: x[2])
    ans = 0
    for i, j, w in edges:
        if not uf.same(i, j):
            uf.unite(i, j)
            ans += w
    print(ans)


__starting_point()
