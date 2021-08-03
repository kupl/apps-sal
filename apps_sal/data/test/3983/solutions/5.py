#!/usr/bin/env python3
import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()


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
        self.all_group_member = defaultdict(list)
        for i in range(self.n):
            self.all_group_member[self.find(i)].append(i)
        return self.all_group_member

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def solve(n, edges):
    if n % 2 == 1:
        numedge = (n * (n - 1)) // 2 - len(edges)
        return 'First' if numedge % 2 == 1 else 'Second'
    else:
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a - 1, b - 1)
        zerolen = uf.size(0) % 2
        nlen = uf.size(n - 1) % 2
        if zerolen != nlen:
            return 'First'
        else:
            oddsize = 0
            for key, value in list(uf.all_group_members().items()):
                if len(value) % 2 == 1:
                    oddsize += 1
            if nlen == 1:
                oddsize -= 2
            numedge = (n * (n - 1)) // 2 - len(edges)
            if numedge % 2 == 1:
                sente_mokuteki = (0, 0)
            else:
                sente_mokuteki = (1, 1)
            return 'First' if sente_mokuteki == (zerolen, nlen) else 'Second'


def main():
    t = int(input())
    for _ in range(t):
        n, m = list(map(int, input().split()))
        edges = [list(map(int, input().split())) for i in range(m)]
        print((solve(n, edges)))


def __starting_point():
    main()


__starting_point()
