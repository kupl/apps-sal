import math


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        left = 1
        right = max(nums)

        while left <= right:
            mid = (left + right) // 2
            sum_val = sum(math.ceil(num / mid) for num in nums)
            if sum_val <= threshold:
                right = mid - 1
            else:
                left = mid + 1
        return left
