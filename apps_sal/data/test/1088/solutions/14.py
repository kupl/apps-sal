import sys
from math import factorial
sys.setrecursionlimit(10**9)
def read(): return sys.stdin.readline()


def read_ints():
    return list(map(int, read().split()))


def read_intgrid(h):
    return list(list(map(int, read().split()))for i in range(h))


class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * n
        self.rank = [0] * n
        self.group_count = n
        self.n = n

    def find(self, x):
        if self.parents[x] < 0:
            return x

        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.rank[x] == self.rank[y]:
            self.parents[x] += self.parents[y]
            self.parents[y] = x
            self.rank[x] += 1

        elif self.rank[x] > self.rank[y]:
            self.parents[x] += self.parents[y]
            self.parents[y] = x
        else:
            self.parents[y] += self.parents[x]
            self.parents[x] = y

        self.group_count -= 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def get_group_member_list(self, x):
        x = self.find(x)
        return [i for i in range(self.n) if self.find(i) == x]

    def get_group_member_count(self, x):
        x = self.find(x)
        return -self.parents[x]

    def get_all_groups(self):
        return {idx: -n for idx, n in enumerate(self.parents) if n < 0}


def f(x):
    tmp = 1
    while x > 0:
        tmp *= x
        x -= 1
    return tmp


def main():
    n, k = map(int, input().split())
    A = read_intgrid(n)

    mod = 998244353

    ans = 1
    uf1 = UnionFind(n)
    uf2 = UnionFind(n)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if all(A[i][c] + A[j][c] <= k for c in range(n)):
                uf1.unite(i, j)
            if all(A[c][i] + A[c][j] <= k for c in range(n)):
                uf2.unite(i, j)

    for k, v in uf1.get_all_groups().items():
        ans *= f(v)
        ans %= mod

    for k, v in uf2.get_all_groups().items():
        ans *= f(v)
        ans %= mod

    return print(ans)


def __starting_point():
    main()


__starting_point()
