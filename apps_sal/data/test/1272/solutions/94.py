import sys
from itertools import combinations


class UnionFind:
    def __init__(self, n):
        self.table = [-1] * n
        self.n = n
        self.inconvenience = n * (n - 1) // 2

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
        self.inconvenience -= d1 * d2
        if d1 <= d2:
            self.table[r2] = r1
            self.table[r1] += d2
        else:
            self.table[r1] = r2
            self.table[r2] += d1


def main():
    input = sys.stdin.buffer.readline
    n, m = list(map(int, input().split()))
    bridges = [tuple([int(x) - 1 for x in input().split()]) for _ in range(m)]
    ans = [0] * m
    ans[-1] = n * (n - 1) // 2
    uf = UnionFind(n)
    for i in range(m - 2, -1, -1):
        uf.union(*bridges[i + 1])
        ans[i] = uf.inconvenience
    for i in range(m):
        print((ans[i]))


def __starting_point():
    main()


__starting_point()
