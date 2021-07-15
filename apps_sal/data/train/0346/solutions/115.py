class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.at_most(nums, k) - self.at_most(nums, k-1)
        
    def at_most(self, nums, k):
        i = 0
        res = 0
        for j, val in enumerate(nums):
            if val &1 == 1:
                k -= 1
            while k < 0:
                if nums[i] &1 == 1:
                    k += 1
                i += 1
            res += j - i + 1
        return res
