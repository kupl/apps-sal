class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        unit = sorted([(s, e) for (s, e) in zip(speed, efficiency)], key=lambda x: x[1], reverse=True)
        max_res = -1
        curr_sum = 0
        MOD = 10 ** 9 + 7
        heap = []
        for (s, e) in unit:
            curr_sum += s
            max_res = max(max_res, curr_sum * e)
            heapq.heappush(heap, s)
            if len(heap) >= k:
                curr_sum -= heapq.heappop(heap)
        return max_res % MOD
