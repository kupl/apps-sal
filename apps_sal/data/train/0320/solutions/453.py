import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        while any(nums):
            if any(x % 2 for x in nums):
                for i in range(len(nums)):
                    if nums[i] != 0 and nums[i] % 2:
                        nums[i] -= 1
                        res += 1
            else:
                nums = [x / 2 for x in nums]
                res += 1
        return res
