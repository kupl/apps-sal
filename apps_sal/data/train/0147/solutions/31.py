import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        lst = sorted(zip(efficiency, speed), reverse = True)
        p = []
        sum_speed = 0
        res = 0
        for e, s in lst:
            sum_speed += s
            heapq.heappush(p, s)
            if len(p) > k:
                sum_speed -= (heapq.heappop(p))
            val = e * sum_speed
            res = max(res, val)
            
        return res % (10**9 + 7)

