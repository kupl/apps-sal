import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        plus_one = times_two = 0
        for idx, num in enumerate(nums):
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

#         1 * 2
#         1 * 2 * 2
#         1 * 2 * 2 * 2
#         1 * 2 * 2 * 2 * 2

#         2^x = 16
#         xln(2) = ln(16)

#         x = ln(n) / ln(2)


#         18

#         0 -> 1
#         1 -> 2
#         2 -> 4
#         4 -> 8
#         8 -> 9
#         9 -> 18
