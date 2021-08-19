import math


class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def posb(m):
            s = 0
            for i in range(len(nums)):
                s += math.ceil(nums[i] / m)
            return s > threshold
        l = 1
        r = 10 ** 9
        while l < r:
            mid = (l + r) // 2
            if posb(mid) == False:
                r = mid
            else:
                l = mid + 1
        return l
