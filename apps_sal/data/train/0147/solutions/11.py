from heapq import *


class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        totalSpeed = 0
        res = 0
        heap = []
        for (e, s) in sorted(zip(efficiency, speed), reverse=True):
            totalSpeed += s
            heappush(heap, s)
            if len(heap) > k:
                totalSpeed -= heappop(heap)
            res = max(res, totalSpeed * e)
        return res % (10 ** 9 + 7)
