import math


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def isDiv(mid):
            s = 0
            for i in nums:
                s += math.ceil(i / mid)
            # print(\"Sum\",s,mid)
            return s <= threshold

        def binsearch():
            low = 1
            high = sum(nums)
            while low < high:
                mid = low + (high - low) // 2
                if isDiv(mid):
                    high = mid
                else:
                    low = mid + 1
            return low
        return binsearch()
