class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
     
        nums.sort()
        n = len(nums)
        left = 0
        right = n - 1
        res = 0
        mod = 10 **9 + 7
        
        while left <=right:
            while left <= right and nums[right] + nums[left] > target:
                right-= 1
            if right < left:
                return res
            res = (res + (1 <<  (right - left))) % mod
            left+= 1
        
        
        return res;
       

