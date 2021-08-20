import numpy as np


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
            return
        if self.parents[x] > self.parents[y]:
            (x, y) = (y, x)
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
        return [i for (i, x) in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, self.members(r)) for r in self.roots()))


(N, M) = list(map(int, input().split()))
uf = UnionFind(N)
A = [0] * M
B = [0] * M
for i in range(M):
    (a, b) = list(map(int, input().split()))
    A[i] = a - 1
    B[i] = b - 1
cmax = int(N * (N - 1) / 2)
FD = [cmax] * (M + 1)
for i in range(M):
    if uf.same(A[M - i - 1], B[M - i - 1]):
        FD[M - i - 1] = FD[M - i]
    else:
        cless = uf.size(A[M - i - 1]) * uf.size(B[M - i - 1])
        FD[M - i - 1] = FD[M - i] - cless
        if FD[M - i - 1] < 0:
            FD[M - i - 1] = 0
    uf.union(A[M - 1 - i], B[M - 1 - i])
for fd in FD[1:]:
    print(fd)
