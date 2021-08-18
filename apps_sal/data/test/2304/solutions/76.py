import sys
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


class UnionFindWeighted:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.weight = [0] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            root = self.find(self.parents[x])
            self.weight[x] += self.weight[self.parents[x]]
            self.parents[x] = root
            return root

    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return

        if self.parents[rx] > self.parents[ry]:
            x, y, rx, ry, w = y, x, ry, rx, -w

        self.parents[rx] += self.parents[ry]
        self.parents[ry] = rx
        self.weight[ry] = self.weight[x] - self.weight[y] - w

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        return self.weight[x] - self.weight[y]


def main():
    N, M, *LRD = list(map(int, read().split()))

    uf = UnionFindWeighted(N)
    for l, r, d in zip(*[iter(LRD)] * 3):
        l -= 1
        r -= 1
        if uf.same(l, r) and uf.diff(l, r) != d:
            print('No')
            return
        else:
            uf.union(l, r, d)

    print('Yes')
    return


def __starting_point():
    main()


__starting_point()
