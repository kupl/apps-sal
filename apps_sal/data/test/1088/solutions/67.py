from collections import defaultdict
from sys import stdin, setrecursionlimit
import bisect
import collections
import copy
import heapq
import itertools
import math
import string
setrecursionlimit(10**8)

INF = float("inf")
MOD = 1000000007


def input():
    return stdin.readline().strip()


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
        group_members = collections.defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in list(self.all_group_members().items()))


def main():

    n, mx = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]

    uf1 = UnionFind(n)
    uf2 = UnionFind(n)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(n):
                if a[i][k] + a[j][k] > mx:
                    break
            else:
                uf1.union(i, j)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(n):
                if a[k][i] + a[k][j] > mx:
                    break
            else:
                uf2.union(i, j)

    ans = 1
    mod = 998244353

    def factorial(n):
        rec = 1
        for x in range(2, n + 1):
            rec *= x
            rec %= mod
        return rec

    for lst in list(uf1.all_group_members().values()):
        ans *= factorial(len(lst))
        ans %= mod

    for lst in list(uf2.all_group_members().values()):
        ans *= factorial(len(lst))
        ans %= mod

    print(ans)

    return


def __starting_point():
    main()


__starting_point()
