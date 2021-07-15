class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        n, res, mod, j = len(nums), 0, 10**9 + 7, len(nums) - 1
        
        for i in range(n):
            while i <= j and nums[i] + nums[j] > target:
                j -= 1
            
            if i <= j and nums[i] + nums[j] <= target:
                res += 2**(j-i) % mod
                res %= mod
        return res
