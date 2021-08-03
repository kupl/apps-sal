from collections import Counter


class Window:
    def __init__(self):
        self.count = Counter()
        self.nonzero = 0

    def add(self, val):
        self.count[val] += 1
        if self.count[val] == 1:
            self.nonzero += 1

    def remove(self, val):
        self.count[val] -= 1
        if self.count[val] == 0:
            self.nonzero -= 1


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        ans = 0
        l1, l2 = 0, 0
        w1, w2 = Window(), Window()
        for r, val in enumerate(A):
            w1.add(val)
            w2.add(val)
            while w1.nonzero > K:
                w1.remove(A[l1])
                l1 += 1
            while w2.nonzero >= K:
                w2.remove(A[l2])
                l2 += 1
            ans += l2 - l1
        return ans
