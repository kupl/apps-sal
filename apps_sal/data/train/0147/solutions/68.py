import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        
        pairs = [(-efficiency[i], speed[i]) for i in range(n)]
        heapq.heapify(pairs)
        t = 0
        res = 0
        usedSpeeds = []
        cur = 0
        while pairs:
            e, s = heapq.heappop(pairs)
            cur += s
            t += 1
            if t <= k:
                res = max(res, -1 * e * cur)
            elif t > k:
                cur -= heapq.heappop(usedSpeeds)
                res = max(res, -1 * e * cur )
            heapq.heappush(usedSpeeds, s)
        return res % (10 ** 9 + 7)
            
                
                
                
                
                
                
                
                
                
            

