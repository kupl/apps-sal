import math


class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        dicti = {0: False}

        def chk(nmb):
            if nmb in dicti:
                return dicti[nmb]
            val = 0
            for num in nums:
                val += math.ceil(num / nmb)
                if val > threshold:
                    dicti[nmb] = False
                    return False
            dicti[nmb] = True
            return dicti[nmb]
        high = sum(nums)
        low = math.ceil(high / threshold)
        while low <= high:
            mid = (low + high) // 2
            if chk(mid):
                high = mid - 1
            elif not chk(mid):
                low = mid + 1
        return low - 1 if chk(low - 1) else high + 1
