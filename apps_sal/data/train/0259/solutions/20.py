import math


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def is_le(divisor):
            count = 0
            for num in nums:
                count += math.ceil(num / divisor)
                if count > threshold:
                    return False
            return True

        low = max(1, math.floor(sum(nums) / threshold))
        high = max(nums)
        while low < high:
            mid = low + (high - low) // 2
            if is_le(mid):
                high = mid
            else:
                low = mid + 1
        return low
