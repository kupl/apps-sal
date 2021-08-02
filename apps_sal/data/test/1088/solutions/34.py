import sys

readline = sys.stdin.readline
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


class UnionFind:
    """
    0-indexed
    """

    from typing import List

    def __init__(self, n):
        from array import array

        self.n = n
        self.parent = array('l', (-1 for _ in range(n)))

    def unite(self, x, y) -> int:
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return 0

        if self.parent[x] > self.parent[y]:
            x, y = y, x

        self.parent[x] += self.parent[y]
        self.parent[y] = x

        return self.parent[x]

    def is_same(self, x, y) -> bool:
        return self.root(x) == self.root(y)

    def root(self, x) -> int:
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def size(self, x) -> int:
        return -self.parent[self.root(x)]

    def groups(self) -> List[List[int]]:
        groups = dict()

        for i in range(self.n):
            p = self.root(i)
            if not groups.get(p):
                groups[p] = []
            groups[p].append(i)

        return list(groups.values())


def main():
    def factorial(x):
        res = 1
        for i in range(1, x + 1):
            res *= i
            res %= MOD
        return res

    def judge1(first, second):
        for i in range(N):
            if grid[first][i] + grid[second][i] > K:
                return False
        return True

    def judge2(first, second):
        for i in range(N):
            if grid[i][first] + grid[i][second] > K:
                return False
        return True

    MOD = 998244353

    N, K = list(map(int, readline().split()))
    grid = []

    for _ in range(N):
        s = list(map(int, readline().split()))
        grid.append(s)

    cnt_r, cnt_c = 1, 1
    uf = UnionFind(N + 1)

    for i in range(N):
        for j in range(i, N):
            if judge1(i, j):
                uf.unite(i, j)

    for gr in uf.groups():
        x = len(gr)
        cnt_r *= factorial(x)
        cnt_r %= MOD

    uf = UnionFind(N + 1)

    for i in range(N):
        for j in range(i, N):
            if judge2(i, j):
                uf.unite(i, j)

    for gr in uf.groups():
        x = len(gr)
        cnt_c *= factorial(x)
        cnt_c %= MOD

    print(((cnt_r * cnt_c) % MOD))


def __starting_point():
    main()


__starting_point()
