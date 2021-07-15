class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        pq, largelst = [], []
        for i in range(n):
            heapq.heappush(pq, (-efficiency[i], speed[i]))
        
        mx, sm = 0, 0
        while pq:
            pop = heapq.heappop(pq)
            eff = -pop[0]
            heapq.heappush(largelst, pop[1])
            sm+=pop[1]
            while len(largelst)>k:
                rm = heapq.heappop(largelst)
                sm -= rm
            mx = max(mx, sm* eff)
            
        return mx % (10**9+7)

