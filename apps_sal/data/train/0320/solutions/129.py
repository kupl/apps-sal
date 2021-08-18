import numpy as np


class Solution:
    def minOperations(self, nums: List[int]) -> int:

        count = 0
        if not any(nums):
            return count
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                nums[i] -= 1
                count += 1
        if any(nums):
            count += 1
            for i in range(len(nums)):
                nums[i] = nums[i] // 2
        return count + self.minOperations(nums)
