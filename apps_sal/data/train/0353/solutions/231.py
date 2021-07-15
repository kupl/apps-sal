class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        total = 0
        MOD = 10**9+7
        lo, hi = 0, len(nums)-1
        
        while lo <= hi:
            if nums[lo] + nums[hi] > target:
                hi -= 1
            else:
                total += pow(2, hi-lo, MOD)
                lo += 1
                
        return total%MOD

