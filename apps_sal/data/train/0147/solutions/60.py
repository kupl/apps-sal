import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        if k < 1:
            return 0
        
        best = 0
        heap = []
        cur_sum = 0
        
        data = sorted(list(zip(speed, efficiency)), key=lambda x: -x[1])
        
        for s, e in data:
            if len(heap) < k:  # always add this eng.
                cur_sum += s
                heapq.heappush(heap, s)
                if cur_sum * e > best:
                    best = cur_sum * e
            else:
                if (cur_sum - heap[0] + s) * e > best:
                    best = (cur_sum - heap[0] + s) * e
                if s > heap[0]:
                    cur_sum += (s - heap[0])
                    heapq.heappush(heap, s)
                    heapq.heappop(heap)
        
        return best % 1000000007

