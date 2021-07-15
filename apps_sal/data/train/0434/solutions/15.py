class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        
        zeroes = 1
        res = 0
        while right < len(nums):
            if nums[right] == 0:
                zeroes -= 1
            
            
            while zeroes < 0:
                if nums[left] == 0:
                    zeroes += 1
                left += 1
            
            res = max(res, right - left)
            right += 1
            
        return res
