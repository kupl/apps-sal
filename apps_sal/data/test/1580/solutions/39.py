from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right


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
    N, M = list(map(int, input().split()))
    uf = UnionFind(N)
    for _ in range(M):
        X, Y, Z = [int(x) - 1 for x in input().split()]
        uf.union(X, Y)
    ans = [uf.find(x) for x in uf.parents]
    print((len(set(ans))))


def __starting_point():
    main()


__starting_point()
