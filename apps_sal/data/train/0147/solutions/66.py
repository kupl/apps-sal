class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        h = []
        res = sSum = 0
        for e, s in sorted(zip(efficiency, speed), reverse=1):
            heapq.heappush(h, s)
            sSum += s
            if len(h) > k:
                sSum -= heapq.heappop(h)
            res = max(res, sSum * e)
        return res % (10**9 + 7)
