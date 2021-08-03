import math


class Solution:
    def minOperations(self, n: List[int]) -> int:
        nums = []
        for i in range(len(n)):
            if n[i] == 0:
                continue
            nums.append(n[i])

        def countOdd(nums):
            c = 0
            for i in range(len(nums)):
                if nums[i] != 1 and nums[i] % 2 == 1:
                    nums[i] -= 1
                    c += 1
            return c
        count = 0
        while set(nums) != {1}:
            count += countOdd(nums)
            for i in range(len(nums)):
                if nums[i] == 1:
                    continue
                nums[i] = nums[i] // 2

            count += 1
        count += len(nums)
        return count
