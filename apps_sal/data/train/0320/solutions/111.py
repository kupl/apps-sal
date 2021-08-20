import math


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        plus_one = times_two = 0
        for (idx, num) in enumerate(nums):
            two = 0
            while num:
                if num == 1:
                    plus_one += 1
                    break
                if num % 2:
                    plus_one += 1
                    num -= 1
                num = num // 2
                two += 1
            times_two = max(times_two, two)
        return plus_one + times_two
