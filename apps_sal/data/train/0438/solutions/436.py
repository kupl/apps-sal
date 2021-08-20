class UF:

    def __init__(self, n):
        self.cnt = [1] * n
        self.fa = [i for i in range(n)]

    def find(self, x):
        if x == self.fa[x]:
            return x
        self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def unit(self, a, b):
        (a, b) = (self.find(a), self.find(b))
        if a == b:
            return False
        if self.cnt[a] < self.cnt[b]:
            (a, b) = (b, a)
        self.cnt[a] += self.cnt[b]
        self.fa[b] = a
        return True

    def count(self, x):
        return self.cnt[self.find(x)]


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        uf = UF(n + 1)
        bits = [0] * (n + 1)
        result = -1
        count = 0
        for (idx, val) in enumerate(arr):
            if val > 1 and bits[val - 1] == 1:
                if uf.count(val - 1) == m:
                    count -= 1
                uf.unit(val, val - 1)
            if val < n and bits[val + 1] == 1:
                if uf.count(val + 1) == m:
                    count -= 1
                uf.unit(val, val + 1)
            if uf.count(val) == m:
                count += 1
            if count > 0:
                result = idx
            bits[val] = 1
        return result + 1 if result != -1 else -1
