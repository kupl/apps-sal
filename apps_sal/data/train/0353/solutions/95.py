class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        nums.sort()
        
        MOD = 10 ** 9 + 7
        
        res = 0
        j = len(nums) - 1
        
        for i in range(len(nums)):
            while i <= j and nums[i] + nums[j] > target:
                j -= 1
                
            if i <= j and nums[i] + nums[j] <= target:
                res = (res + 2 ** (j - i))
                if res >= MOD:
                    res -= MOD
            
        return res % MOD
