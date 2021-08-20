import math


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        res = 0
        while sum(nums) != 0:
            counts = sum([x % 2 == 0 for x in nums])
            if counts == len(nums):
                for i in range(len(nums)):
                    nums[i] = nums[i] // 2
                res += 1
            else:
                for i in range(len(nums)):
                    if nums[i] % 2 != 0:
                        nums[i] -= 1
                        res += 1
        return res
