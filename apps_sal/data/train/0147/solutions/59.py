from heapq import heappush, heappop

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        speed_heap = []
        speed_sum = 0
        max_performance = 0

        for cur_efficiency, cur_speed in sorted(zip(efficiency, speed), reverse=True):
            heappush(speed_heap, cur_speed)
            speed_sum += cur_speed

            if len(speed_heap) > k:
                speed_sum -= heappop(speed_heap)

            max_performance = max(max_performance, speed_sum * cur_efficiency)

        return max_performance % (10 ** 9 + 7)
