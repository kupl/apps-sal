from heapq import *

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        N = len(quality)
        
        workers = [(wage[i] / float(quality[i]), quality[i]) for i in range(N)]
        workers = sorted(workers)
        
        # sum_ = sum([x[1] for x in prices_per_unit[:K - 1]])
        
        # print(prices_per_unit)
        
        result = float('inf')
        sum_ = 0
        max_heap = []
        for i in range(K - 1):
            heappush(max_heap, -workers[i][1])
            sum_ += workers[i][1]
            
        for i in range(K - 1, len(workers)):
            result = min(result, (sum_ + workers[i][1]) * workers[i][0])
            if len(max_heap) > 0 and workers[i][1] < -max_heap[0]:
                sum_ -= (-heappop(max_heap))
                sum_ += workers[i][1]
                heappush(max_heap, -workers[i][1])
        
        return result
    

