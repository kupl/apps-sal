class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10**9 + 7

        order = sorted(range(n), key=lambda i: efficiency[i], reverse=True)

        heap = []
        filled = 0
        rec = 0
        speed_sum = 0

        for i in order:
            if filled < k:
                heapq.heappush(heap, speed[i])
                filled += 1
                speed_sum += speed[i]
            else:
                removed = heapq.heappushpop(heap, speed[i])
                speed_sum += speed[i] - removed
            rec = max(rec, speed_sum * efficiency[i])

        return rec % mod
