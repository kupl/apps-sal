import math

class Solution:
    
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        res = 0
        md = 10**9+7
        
        while left <= right:
            if nums[left] + nums[right] <= target:
               
                res += pow(2, right - left) 
                left += 1
            else:
                right -= 1
        return res % md
