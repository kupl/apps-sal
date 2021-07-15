from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mindeque = deque()
        maxdeque = deque()
        
        L = R = 0
        res = 0
        
        while R < len(nums):
            while mindeque and nums[mindeque[-1]] > nums[R]:
                mindeque.pop()
            mindeque.append(R)
            
            while maxdeque and nums[maxdeque[-1]] < nums[R]:
                maxdeque.pop()
            maxdeque.append(R)
            
            if nums[maxdeque[0]] - nums[mindeque[0]] <= limit:
                res = max(res, R - L + 1)
            else:
                while nums[maxdeque[0]] - nums[mindeque[0]] > limit:
                    if L == maxdeque[0]:
                        maxdeque.popleft()
                    if L == mindeque[0]:
                        mindeque.popleft()
                    L += 1
            R += 1
        
        return res
