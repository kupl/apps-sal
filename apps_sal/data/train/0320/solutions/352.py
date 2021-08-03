class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        while any(nums):
            for i, n in enumerate(nums):
                if n & 1:
                    nums[i] -= 1
                    res += 1
                nums[i] >>= 1
            res += any(nums)
        return res
