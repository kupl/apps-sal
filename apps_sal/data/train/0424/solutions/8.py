
from functools import lru_cache
from copy import deepcopy


@lru_cache(None)
def countBits(n):
    return 0 if n == 0 else (n & 1) + countBits(n >> 1)


class Solution:
    def stateCompress(self, img):
        n, m = len(img), len(img[0])
        rows = [0 for _ in range(n)]
        for i, row in enumerate(img):
            for e in row:
                rows[i] = (rows[i] << 1) + e
        return n, m, rows

    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n, m, rA = self.stateCompress(A)
        _, _, rB = self.stateCompress(B)

        def shift(arr1, arr2, l):
            return sum(countBits(e1 & e2) for e1, e2 in zip(arr1[:l], arr2[n - l:n]))

        maxOverLap = 0
        tA = deepcopy(rA)
        tB = deepcopy(rB)

        for dc in range(m):
            for dr in range(1, n + 1):
                maxOverLap = max(maxOverLap, shift(tA, rB, dr))
                maxOverLap = max(maxOverLap, shift(tB, rA, dr))
            tA = [e >> 1 for e in tA]
            tB = [e >> 1 for e in tB]
        return maxOverLap
