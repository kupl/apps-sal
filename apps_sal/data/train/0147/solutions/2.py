from heapq import *


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        engineers = sorted(zip(speed, efficiency), key=lambda x: -x[1])
        min_heap = []
        max_performance = 0
        curr_speed_sum = 0
        for i in range(len(engineers)):
            speed = engineers[i][0]
            efficiency = engineers[i][1]

            if len(min_heap) < k:
                curr_speed_sum += speed
                heappush(min_heap, speed)
            else:
                if speed > min_heap[0]:
                    top_kth_speed = heappushpop(min_heap, speed)
                    curr_speed_sum -= top_kth_speed
                    curr_speed_sum += speed
                else:
                    continue

            max_performance = max(max_performance, curr_speed_sum * efficiency)

        return max_performance % (10 ** 9 + 7)
