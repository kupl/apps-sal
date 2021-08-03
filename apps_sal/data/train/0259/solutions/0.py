import numpy as np
import math


class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if len(nums) == 1:
            return int(math.ceil(nums[0] / threshold))

        np_nums = np.array(nums)
        low, high = 1, np.max(np_nums)

        divisors = []
        while low + 1 < high:
            mid = (low + high) // 2

            if np.sum(np.ceil(np_nums / mid)) > threshold:
                low = mid
            else:
                high = mid

        if np.sum(np.ceil(np_nums / low)) <= threshold:
            return low

        return high
