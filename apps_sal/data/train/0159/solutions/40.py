from heapq import heappush, heappop

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # [-max_sum, idx]
        
        res = -float('inf')
        queue = []
        for i, x in enumerate(nums):
            while queue and queue[0][1] < i - k:
                heappop(queue)
                
            if queue:
                y = x - queue[0][0]
            else:
                y = x
            
            res = max(res, y)
            if y > 0:
                heappush(queue, [-y, i])
                
        return res
