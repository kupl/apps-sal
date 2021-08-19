class Solution:

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        while any((v > 0 for v in nums)):
            for (i, v) in enumerate(nums):
                if v & 1:
                    res += 1
                nums[i] >>= 1
            res += 1
        return res - 1
