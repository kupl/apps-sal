from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start = 0
        n = len(nums)
        k = limit
        s = SortedList()
        
        max_count = 0
        
        for i in range(n):
            
            s.add(nums[i])
            
            if s[-1] - s[0] > k:
                while s[-1] - s[0] > k:
                    s.remove(nums[start])
                    start += 1
            max_count = max(max_count, len(s))
        
        return max_count
            

