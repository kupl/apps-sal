import heapq

class Solution:
    def mincostToHireWorkers_tle(self, quality: List[int], wage: List[int], K: int) -> float:
        ans = float('inf')
        
        for i in range(len(quality)):
            factor = wage[i] / quality[i]
            
            prices = []
            for i in range(len(quality)):
                if factor * quality[i] >= wage[i]:
                    prices.append(factor * quality[i])
                
            if len(prices) < K:
                continue
            
            prices.sort()
            
            ans = min(ans, sum(prices[:K]))
            
        return ans
    
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        if not quality: return 0
        
        workers = sorted([(wage[i] / quality[i], quality[i], wage[i]) for i in range(len(quality))])
        
        min_cost = float('inf')
        total = 0
        k_workers = []
        for w in workers:
            total += w[1]
            heapq.heappush(k_workers, -w[1])
            
            if len(k_workers) > K:
                total += heapq.heappop(k_workers)
            
            if len(k_workers) == K:
                min_cost = min(min_cost, total * w[0])
                
            
            
                
        return min_cost
            
                
            
                

