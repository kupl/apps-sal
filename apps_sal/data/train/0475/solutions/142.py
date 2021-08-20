import math


class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        nums.append(0)
        total = 0
        for i in range(len(nums)):
            temp = nums[i]
            nums[i] = total
            total += temp
        nums[-1] = total
        sums = []
        for i in range(1, len(nums)):
            for j in range(i):
                value = nums[i] - nums[j]
                sums.append(value % (10 ** 9 + 7))
        sums.sort()
        total = 0
        for i in range(left - 1, right):
            total += sums[i]
        return total % (10 ** 9 + 7)
