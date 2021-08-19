class UF:

    def __init__(self, N):
        self.N = N
        self.size = [0] * N
        self.stat = [False] * N
        self.id = list(range(N))
        self.sizes = collections.Counter()

    def find(self, x):
        if self.id[x] != x:
            self.id[x] = self.find(self.id[x])
        return self.id[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.size[px] += self.size[py]
            self.id[py] = px
            self.sizes[self.size[py]] -= 1

    def set(self, x):
        self.stat[x] = True
        self.size[x] += 1
        if x - 1 >= 0 and self.stat[x - 1]:
            self.union(x, x - 1)
        if x + 1 < self.N and self.stat[x + 1]:
            self.union(x, x + 1)
        self.sizes[self.size[x]] += 1


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        uf = UF(n)
        ans = -1
        for (step, idx) in enumerate(arr, 1):
            uf.set(idx - 1)
            if uf.sizes[m] > 0:
                ans = step
        return ans
