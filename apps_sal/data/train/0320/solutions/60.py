import math


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        (ones, co, twos) = (0, 0, 0)
        for xx in nums:
            (x, c) = (0, 0)
            while xx > 1:
                co += xx & 1
                xx //= 2
                c += 1
            x = int(floor(math.log(max(xx, 1), 2)))
            twos = max(twos, x + c)
            ones += max(xx - 2 ** x, 0)
            if xx >= 1:
                ones += 1
        return ones + twos + co
