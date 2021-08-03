from collections import Counter


class DSU:
    def __init__(self, n):
        self.par = [x for x in range(n)]
        self.sz = [1] * n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp == yp:
            return False
        if self.sz[xp] < self.sz[yp]:
            xp, yp = yp, xp

        self.par[yp] = xp
        self.sz[xp] += self.sz[yp]
        self.sz[yp] = self.sz[xp]
        return True

    def size(self, x):
        xp = self.find(x)
        return self.sz[xp]


class Solution:
    def findLatestStep(self, arr, m):
        res = -1
        n = len(arr)
        dsu = DSU(n)

        A = [0] * n
        count = Counter()
        for i, x in enumerate(arr, start=1):
            x -= 1
            A[x] = 1
            this = 1
            if x - 1 >= 0 and A[x - 1]:
                left = dsu.size(x - 1)
                dsu.union(x, x - 1)
                this += left
                count[left] -= 1
            if x + 1 < n and A[x + 1]:
                right = dsu.size(x + 1)
                dsu.union(x, x + 1)
                this += right
                count[right] -= 1

            count[this] += 1
            if count[m] > 0:
                res = i
        return res
