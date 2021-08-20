class DSU:

    def __init__(self):
        self.p = {}
        self.r = {}
        self.count = collections.Counter()

    def add(self, x: int):
        self.p[x] = x
        self.r[x] = 1
        self.count[1] += 1

    def parent(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.parent(self.p[x])
        return self.p[x]

    def unite(self, x: int, y: int) -> int:
        x = self.parent(x)
        y = self.parent(y)
        if x == y:
            return self.r[x]
        if self.r[x] > self.r[y]:
            (x, y) = (y, x)
        self.count[self.r[x]] -= 1
        self.count[self.r[y]] -= 1
        self.count[self.r[x] + self.r[y]] += 1
        self.p[x] = y
        self.r[y] += self.r[x]
        return self.r[y]


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        dsu = DSU()
        bits = [0] * (n + 2)
        ans = -1
        for (i, bit) in enumerate(arr, 1):
            dsu.add(bit)
            bits[bit] = 1
            if bits[bit - 1] == 1:
                dsu.unite(bit, bit - 1)
            if bits[bit + 1] == 1:
                dsu.unite(bit, bit + 1)
            if dsu.count[m] > 0:
                ans = i
        return ans
