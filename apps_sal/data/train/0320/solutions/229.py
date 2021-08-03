class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # print()

        res = 0
        while any(nums):
            ones = sum(num & 1 for num in nums)
            res += ones
            nums = [num >> 1 for num in nums]
            res += 1
            # print(ones, nums, res)

        return res - 1
