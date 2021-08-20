import math


class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def get_sum(nmb):
            if nmb == 0:
                return False
            val = 0
            for num in nums:
                val += math.ceil(num / nmb)
            return val
        (left, right) = (1, max(nums))
        while left <= right:
            mid = (left + right) // 2
            if get_sum(mid) > threshold:
                left = mid + 1
            else:
                right = mid - 1
        if get_sum(left) <= threshold:
            return left
        return right
