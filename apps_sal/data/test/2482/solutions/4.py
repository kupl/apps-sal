from collections import Counter


class UnionFind:
    def __init__(self, n):
        self.table = [-1] * n

    def _root(self, x):
        stack = []
        tbl = self.table
        while tbl[x] >= 0:
            stack.append(x)
            x = tbl[x]
        for y in stack:
            tbl[y] = x
        return x

    def find(self, x, y):
        return self._root(x) == self._root(y)

    def union(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            self.table[r1] += d2
        else:
            self.table[r1] = r2
            self.table[r2] += d1


def main():
    n, k, l = list(map(int, input().split()))
    a = UnionFind(n)
    b = UnionFind(n)
    for _ in range(k):
        p, q = list(map(int, input().split()))
        a.union(p-1, q-1)
    for _ in range(l):
        r, s = list(map(int, input().split()))
        b.union(r-1, s-1)
    d = Counter((a._root(i), b._root(i)) for i in range(n))
    print((*(d[(a._root(i), b._root(i))] for i in range(n))))


def __starting_point():
    main()

__starting_point()
