import math


class Solution:

    def rec(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            if nums[0] <= 2:
                return nums[0]
            if nums[0] % 2 == 0:
                nums[0] = nums[0] // 2
                return 1 + self.rec(nums)
            else:
                nums[0] = (nums[0] - 1) // 2
                return 2 + self.rec(nums)
        op = 0
        new = []
        for i in range(len(nums)):
            if nums[i] != 0:
                if nums[i] % 2 != 0:
                    nums[i] -= 1
                    op += 1
                    if nums[i] != 0:
                        new.append(nums[i] // 2)
                else:
                    new.append(nums[i] // 2)
        if len(new) > 0:
            op += 1
        return op + self.rec(new)

    def minOperations(self, nums: List[int]) -> int:
        return self.rec(nums)
