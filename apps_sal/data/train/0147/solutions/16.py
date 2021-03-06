class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        es = list(zip(efficiency, speed))
        es.sort(reverse=True)
        speed_sum = 0
        max_prod = 0
        heap = []
        for i in range(k):
            (eff, speed) = es[i]
            speed_sum += speed
            max_prod = max(max_prod, speed_sum * eff)
            heap.append(speed)
        heapq.heapify(heap)
        for i in range(k, n):
            (cur_eff, cur_speed) = es[i]
            heapq.heappush(heap, cur_speed)
            speed_sum -= heapq.heappop(heap)
            speed_sum += cur_speed
            max_prod = max(max_prod, speed_sum * cur_eff)
        return max_prod % (10 ** 9 + 7)
