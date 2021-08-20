import sys
from collections import defaultdict
from typing import List


class Solution:

    def maxValueAfterReverse(self, nums: List[int]) -> int:
        result = 0
        gain = -sys.maxsize
        hi = -sys.maxsize
        lo = sys.maxsize
        for index in range(len(nums) - 1):
            n1 = nums[index]
            n2 = nums[index + 1]
            result += abs(n1 - n2)
            gain1 = -abs(n1 - n2) + abs(n2 - nums[0])
            gain2 = -abs(n1 - n2) + abs(n1 - nums[-1])
            gain = max(gain, gain1, gain2)
            hi = max(hi, min(n1, n2))
            lo = min(lo, max(n1, n2))
        newgain = 2 * (hi - lo)
        result += max(gain, newgain)
        return result
