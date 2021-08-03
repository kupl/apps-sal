import sys
import numpy as np
from itertools import combinations


class UnionFind:
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
            return False
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return True

    def roots_size(self):
        return [-x for x in self.parents if x < 0]

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    mod = 998244353
    n, k = map(int, input().split())
    A = np.array(sys.stdin.read().split(), dtype=np.int64).reshape((n, -1))
    uf_r = UnionFind(n)
    uf_c = UnionFind(n)
    for i, j in combinations(range(n), 2):
        if np.all(A[i, :] + A[j, :] <= k):
            uf_r.union(i, j)
        if np.all(A[:, i] + A[:, j] <= k):
            uf_c.union(i, j)
    s = 1
    factorial_table = [1]
    for i in range(1, n + 1):
        s *= i
        s %= mod
        factorial_table.append(s)
    ans = 1
    for size in uf_r.roots_size() + uf_c.roots_size():
        ans *= factorial_table[size]
        ans %= mod
    print(ans)


def __starting_point():
    main()


__starting_point()
