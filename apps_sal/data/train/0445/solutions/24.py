from heapq import heappush, heappop

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        max_h = []
        min_h = []
        
        for i in nums:
            heappush(max_h, i)
            heappush(min_h, -i)
            
            if len(max_h) > 4:
                heappop(max_h)
                heappop(min_h)

            
                
        min_h = [-item for item in min_h]
        
        max_h.sort()
        min_h.sort()
        
        return min([max_h[i] - min_h[i] for i in range(len(max_h))])
