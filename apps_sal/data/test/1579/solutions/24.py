import sys
from collections import Counter

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


class UnionFind:
    # Reference: https://note.nkmk.me/python-union-find/
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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.parents[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}


def main():
    N, *XY = list(map(int, read().split()))

    MAX = 100010
    uf = UnionFind(MAX * 2)
    for x, y in zip(*[iter(XY)] * 2):
        uf.union(x, y + MAX)

    x_comp = Counter()
    y_comp = Counter()
    for i in range(MAX):
        x_comp[uf.find(i)] += 1
    for i in range(MAX, 2 * MAX):
        y_comp[uf.find(i)] += 1

    ans = 0
    for k in list(x_comp.keys()):
        ans += x_comp[k] * y_comp[k]

    ans -= N

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
