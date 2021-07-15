from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        queue = deque()
        res = float('-inf')
        
        for i in range(n):
            
            if queue and i - queue[0][1] > k:
                queue.popleft()
            
            cur = nums[i] + max(0, (queue[0][0] if queue else 0))
            res = max(res, cur)
            
            while queue and queue[-1][0] <= cur:
                queue.pop()
            queue.append((cur, i))
                
        return res

