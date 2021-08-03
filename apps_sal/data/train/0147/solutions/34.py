import heapq


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        res = 0
        hired, curr_sum = [], 0
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            heapq.heappush(hired, s)
            curr_sum += s
            if len(hired) > k:
                curr_sum -= heapq.heappop(hired)
            res = max(res, curr_sum * e)
        return res % (10**9 + 7)
