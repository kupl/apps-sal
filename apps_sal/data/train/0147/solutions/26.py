class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        h = []
        ssum = 0
        res = 0
        for (e, s) in sorted(zip(efficiency, speed), reverse=True):
            heapq.heappush(h, s)
            ssum += s
            if len(h) > k:
                ssum -= heapq.heappop(h)
            res = max(res, ssum * e)
        return res % (10 ** 9 + 7)
