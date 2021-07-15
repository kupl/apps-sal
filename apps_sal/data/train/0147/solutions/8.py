from heapq import heappush,heappop

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        comb = sorted(zip(efficiency,speed), reverse = True)
        min_heap = []
        perf = 0
        s = 0
        for i in range(n):
            heappush(min_heap,comb[i][1])
            s += comb[i][1]
            if i >= k:
                s -= heappop(min_heap)
                
            perf = max(perf, s * comb[i][0])
        
        return perf % (10 ** 9 + 7)
