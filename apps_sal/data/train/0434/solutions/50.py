class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
        zero_seen = False
        for i in range(len(nums)):
            length = 0
            if nums[i] == 0:
                zero_seen = True
                l,r = i-1, i+1
                while l >= 0 and nums[l] == 1:
                    length += 1
                    l -=1
                while r < len(nums) and nums[r] == 1:
                    length += 1
                    r += 1
                max_len = max(max_len, length)
        
        return max_len if zero_seen else len(nums)-1
