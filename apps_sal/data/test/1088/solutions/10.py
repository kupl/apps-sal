import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate

sys.setrecursionlimit(10**6)
INF = 10**12
m = 998244353


class UnionFind():
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                x, y = y, x
            self.parents[y] = x
            self.size[x] += self.size[y]


def main():
    N, K = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 1

    p = 998244353
    a = [None] * (N + 1)
    inva = [None] * (N + 1)
    a[0] = 1

    for i in range(1, N + 1):
        a[i] = i * a[i - 1] % p

    inva[N] = pow(a[N], p - 2, p)
    for i in range(N):
        inva[N - i - 1] = inva[N - i] * (N - i) % p

    rowuf = UnionFind(N)
    for x in range(N):
        for y in range(x + 1, N):
            for i in range(N):
                if A[i][x] + A[i][y] > K:
                    break
            else:
                rowuf.union(x, y)

    rows = []
    for i in range(N):
        rows.append(rowuf.find(i))

    for l in list(Counter(rows).values()):
        ans *= a[l]
        ans %= p

    coluf = UnionFind(N)
    for x in range(N):
        for y in range(x + 1, N):
            for i in range(N):
                if A[x][i] + A[y][i] > K:
                    break
            else:
                coluf.union(x, y)
    cols = []
    for i in range(N):
        cols.append(coluf.find(i))

    for l in list(Counter(cols).values()):
        ans *= a[l]
        ans %= p

    print(ans)


def __starting_point():
    main()


__starting_point()
