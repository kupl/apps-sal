import copy
import math


class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        (positive, negative) = (0, 0)
        length = 0
        for n in nums:
            if n == 0:
                (positive, negative) = (0, 0)
            elif n > 0:
                if negative > 0:
                    (positive, negative) = (positive + 1, negative + 1)
                else:
                    (positive, negative) = (positive + 1, 0)
            elif negative > 0:
                (positive, negative) = (negative + 1, positive + 1)
            else:
                (positive, negative) = (0, positive + 1)
            length = max(length, positive)
        return length
