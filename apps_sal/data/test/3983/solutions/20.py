import sys
import math

input = sys.stdin.readline
T = int(input())


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
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


for _ in range(T):
    N, M = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(M)]
    uf = UnionFind(N)
    for a, b in ab:
        a -= 1
        b -= 1
        uf.union(a, b)
    roots_size = [uf.size(i) % 2 for i in uf.roots()]
    s_size = uf.size(0) % 2
    t_size = uf.size(N - 1) % 2
    flg = (N * (N - 1) // 2 - M) % 2
    if N % 2 == 1:
        flg = flg ^ 0
        if flg:
            print('First')
        else:
            print('Second')
    else:
        if sum(roots_size) == (s_size + t_size):
            flg = flg ^ (s_size & t_size)
        else:
            if (s_size & t_size):
                flg = flg ^ 1
            elif not (s_size | t_size):
                flg = flg ^ 0
            else:
                flg = 1
        if flg:
            print('First')
        else:
            print('Second')
