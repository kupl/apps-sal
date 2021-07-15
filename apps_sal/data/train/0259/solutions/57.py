import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def division(divisor):
            total = 0
            for n in nums:
                total += math.ceil(n / divisor)
            return total
        
        total = sum(nums)
        left = max(1, total//threshold)
        right = math.ceil(total/(threshold-len(nums)))
        while left < right:
            mid = (left + right) // 2
            if division(mid) > threshold:
                left = mid + 1
            else:
                right = mid
        return left

