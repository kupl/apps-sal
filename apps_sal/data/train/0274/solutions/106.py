import collections
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minq = collections.deque()
        maxq = collections.deque()
        j = 0
        count = 0
        for i, val in enumerate(nums):
            
            while len(minq) > 0 and minq[-1] > val:
                minq.pop()
            while len(maxq) > 0 and maxq[-1] < val:
                maxq.pop()
                
            minq.append(val)
            maxq.append(val)
            
            
            while len(minq) > 0 and len(maxq) > 0 and maxq[0] - minq[0] > limit:
                if nums[j] == maxq[0]:
                    maxq.popleft()
                    
                if nums[j] == minq[0]:
                    minq.popleft()
                    
                j += 1
                
            count = max(count, i - j + 1)
            
        return count

