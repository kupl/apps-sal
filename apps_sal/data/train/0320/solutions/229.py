class Solution:

    def minOperations(self, nums: List[int]) -> int:
        res = 0
        while any(nums):
            ones = sum((num & 1 for num in nums))
            res += ones
            nums = [num >> 1 for num in nums]
            res += 1
        return res - 1
