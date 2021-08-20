import numpy as np


class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        Nums = np.array(nums)
        low = 1
        high = np.max(Nums)
        min_num = np.max(Nums)
        Sum = 0
        while low <= high:
            mid = np.ceil((low + high) / 2)
            Sum = np.sum(np.ceil(Nums / mid))
            if Sum <= threshold:
                min_num = mid
                high = mid - 1
            else:
                low = mid + 1
        return int(min_num)
