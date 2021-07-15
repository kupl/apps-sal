class Solution:
    def numSubarraysWithSum(self, nums: List[int], target: int) -> int:
        return self._at_most(nums, target) - self._at_most(nums, target - 1)
    
    def _at_most(self, nums, target):
        cnt = 0
        sums = 0
        i = 0
        for j in range(len(nums)):
            sums += nums[j]
            
            while i <= j and sums > target:
                sums -= nums[i]
                i += 1
            
            if sums <= target:
                cnt += j - i + 1
            
        return cnt
