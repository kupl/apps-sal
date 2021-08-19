import sys
import math


def input():
    return sys.stdin.readline().rstrip()


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

    def all_family_count(self):
        return [-min(0, x) for (i, x) in enumerate(self.parents)]


def main():
    (N, K) = list(map(int, input().split()))
    mod = 998244353
    A = [[] for _ in range(N)]
    for i in range(N):
        a = list(map(int, input().split()))
        A[i] = a
    row = UnionFind(N)
    column = UnionFind(N)
    for i in range(N - 1):
        for j in range(i + 1, N):
            for w in range(N):
                if A[i][w] + A[j][w] > K:
                    break
            else:
                row.union(i, j)
    for i in range(N - 1):
        for j in range(i + 1, N):
            for w in range(N):
                if A[w][i] + A[w][j] > K:
                    break
            else:
                column.union(i, j)
    root_row = row.all_family_count()
    ans_row = 1
    for i in range(N):
        k = root_row[i]
        ans_row *= math.factorial(k)
    root_column = column.all_family_count()
    ans_column = 1
    for i in range(N):
        k = root_column[i]
        ans_column *= math.factorial(k)
    print(ans_column * ans_row % mod)


def __starting_point():
    main()


__starting_point()
