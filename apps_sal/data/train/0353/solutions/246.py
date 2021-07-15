class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        j = len(nums) - 1
        mod = 10**9 + 7
        for i in range(len(nums)):
            while i <= j and nums[i] + nums[j] > target:
                j -= 1
            
            if i <= j and nums[i] + nums[j] <= target:
                count += pow(2, j-i, mod)
                count = count % mod
                
        return count
