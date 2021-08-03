"""Minimum spanning tree with Kruskal's algorithm"""
import sys


class UnionFind:
    def __init__(self, n):
        # total number of nodes.
        self.n = n
        # node id -> root node id
        self._root_table = list(range(n))
        # root node id -> group size
        self._size_table = [1] * n

    def find(self, x):
        """Returns x's root node id."""
        r = self._root_table[x]
        if r != x:
            # Update the cache on query.
            r = self._root_table[x] = self.find(r)
        return r

    def union(self, x, y):
        """Merges two groups."""
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        # Ensure that x is the larger (or equal) group.
        if self._size_table[x] < self._size_table[y]:
            x, y = y, x

        self._size_table[x] += self._size_table[y]
        self._root_table[y] = x

    def size(self, x):
        return self._size_table[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self._root_table) if x == i]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return "\n".join("{}: {}".format(r, self.members(r)) for r in self.roots())


input = sys.stdin.readline


def main():
    N = int(input())
    cities, xs, ys = [], [], []
    for i in range(N):
        x, y = list(map(int, input().split()))
        cities.append((x, y))
        xs.append((x, i))
        ys.append((y, i))
    xs.sort()
    ys.sort()
    xd, yd = [], []
    for i in range(1, N):
        x1, c1 = xs[i - 1]
        x2, c2 = xs[i]
        if x2 - x1 <= abs(cities[c1][1] - cities[c2][1]):
            xd.append((x2 - x1, c1, c2))
        y1, c1 = ys[i - 1]
        y2, c2 = ys[i]
        if y2 - y1 < abs(cities[c1][0] - cities[c2][0]):
            xd.append((y2 - y1, c1, c2))
    xd.sort()

    uf = UnionFind(N)
    cost = 0
    merged_cnt = 0
    for d1, c1, c2 in xd:
        if not uf.same(c1, c2):
            uf.union(c1, c2)
            cost += d1
            merged_cnt += 1
            if merged_cnt == N - 1:
                break
    print(cost)


def __starting_point():
    main()


__starting_point()
