from heapq import heappop, heappush


class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        queue = []
        sspeed = 0
        res = 0
        for (e, s) in sorted(zip(efficiency, speed), reverse=True):
            heappush(queue, s)
            sspeed += s
            if len(queue) > k:
                sspeed -= heappop(queue)
            res = max(res, sspeed * e)
        return res % (10 ** 9 + 7)
