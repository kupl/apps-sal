class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        q = []
        sum_speed = 0
        res = 0
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            sum_speed += s
            heapq.heappush(q, s)
            while len(q) > k:
                sum_speed -= heapq.heappop(q)
            res = max(res, e * sum_speed)
        return res % (10 ** 9 + 7)
