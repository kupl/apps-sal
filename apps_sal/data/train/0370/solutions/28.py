class UFDS:
    def __init__(self, n, nums):
        self.p = list(range(n + 1))
        self.size = [0] * (n + 1)
        for num in nums:
            self.size[num] = 1

    def find(self, n):
        if n != self.p[n]:
            self.p[n] = self.find(self.p[n])
        return self.p[n]

    def union(self, i, j):
        p1 = self.find(i)
        p2 = self.find(j)
        if p1 != p2:
            if self.size[p1] > self.size[p2]:
                self.p[p2] = p1
                self.size[p1] += self.size[p2]
            else:
                self.p[p1] = p2
                self.size[p2] += self.size[p1]


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        hi = max(A)
        ufds = UFDS(hi, A)
        isPrime = [True] * (hi + 1)
        for i in range(2, hi + 1):
            if not isPrime[i]:
                continue
            for j in range(2 * i, hi + 1, i):
                isPrime[j] = False
                if ufds.size[j]:
                    ufds.union(i, j)
        return max(ufds.size)
