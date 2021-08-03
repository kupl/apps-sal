from collections import Counter


class UnionFind:

    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.ranks = [0] * size

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp == yp:
            return
        if self.ranks[xp] < self.ranks[yp]:
            self.parents[xp] = yp
        elif self.ranks[xp] > self.ranks[yp]:
            self.parents[yp] = xp
        else:
            self.parents[xp] = yp
            self.ranks[yp] += 1


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:

        if not A:
            return 0

        n = max(A)
        dsu = UnionFind(n + 1)

        for a in A:
            for k in range(2, int(a**0.5) + 1):
                if a % k == 0:
                    dsu.union(a, k)
                    dsu.union(a, a // k)

        return max(Counter([dsu.find(a) for a in A]).values())
