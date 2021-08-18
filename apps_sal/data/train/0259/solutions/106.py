import math


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def chk(nmb):
            if nmb == 0:
                return False
            val = 0
            for num in nums:
                val += math.ceil(num / nmb)
            return val <= threshold

        high = max(nums)
        low = high // threshold
        while low <= high:
            mid = (low + high) // 2

            if chk(mid):
                high = mid - 1
            elif not chk(mid):
                low = mid + 1
        return high + 1 if chk(high + 1) else high
