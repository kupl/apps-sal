import sortedcontainers

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        window = sortedcontainers.SortedList()
        N = len(nums)
        
        left = 0
        right = -1
        
        def check():
            if not window: 
                return True
            return window[-1] - window[0] <= limit
        
        ret = 1
        
        while left < N and right < N:
            if not check():
                window.remove(nums[left])
                left += 1
            else:
                ret = max(ret, right - left  + 1)
                right += 1
                if right < N:
                    window.add(nums[right])
        
        return ret
