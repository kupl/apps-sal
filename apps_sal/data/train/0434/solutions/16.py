class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i, j = 0, 0
        ans, cur = 0, 0
        while j < len(nums):
            cur += nums[j]
            while i < j and cur < j-i:
                cur -= nums[i]
                i += 1
            ans = max(ans, cur)            
            j += 1
        return min(ans, len(nums)-1)
                
            

