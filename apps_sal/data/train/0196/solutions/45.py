import math


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total = 0
        maxss, maxss_cur = -math.inf, -math.inf
        minss, minss_cur = 0, 0
        for a in A:
            maxss_cur = a + max(maxss_cur, 0)
            maxss = max(maxss, maxss_cur)

            minss_cur = a + min(minss_cur, 0)
            minss = min(minss, minss_cur)

            total += a

        return maxss if total == minss else max(maxss, total - minss)
