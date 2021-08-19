#
# @lc app=leetcode id=835 lang=python3
#
# [835] Image Overlap
#

# @lc code=start
from functools import lru_cache


@lru_cache
def countBits(n):
    if n == 0:
        return 0
    return (n & 1) + countBits(n >> 1)


class Solution:
    def stateCompress(self, img):
        n, m = len(img), len(img[0])
        rows = [0 for _ in range(n)]
        for i, row in enumerate(img):
            for j, e in enumerate(row):
                rows[i] = (rows[i] << 1) + e
        return n, m, rows

    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n, m, rA = self.stateCompress(A)
        _, _, rB = self.stateCompress(B)

        def shift(xAs, xAe, xBs, xBe, dy):
            if dy > 0:
                return (countBits((e1 << dy) & e2) for e1, e2 in zip(rA[xAs:xAe], rB[xBs:xBe]))
            else:
                dy = -dy
                return (countBits((e1 >> dy) & e2) for e1, e2 in zip(rA[xAs:xAe], rB[xBs:xBe]))

        print((rA, rB))
        maxOverLap = 0
        for dr in range(n):
            for dc in range(m):
                maxOverLap = max(maxOverLap, sum(shift(dr, n, 0, n - dr, dc)))
                maxOverLap = max(maxOverLap, sum(shift(0, dr, n - dr, n, dc)))
                maxOverLap = max(maxOverLap, sum(shift(dr, n, 0, n - dr, -dc)))
                maxOverLap = max(maxOverLap, sum(shift(0, dr, n - dr, n, -dc)))
        return maxOverLap


# @lc code=end
