import math


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        t = 0
        h = nums[0]
        for n in nums:
            if n > h:
                h = n
            while n:
                n &= n - 1
                t += 1
        if h > 0:
            return t + math.floor(math.log(h, 2))
        return t
