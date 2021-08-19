import math


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # No matter what each num must contribute at least 1 (even if the divisor is infinite)
        # We need to binary search divisor range from 1 to max(nums), since the lowest divisor possible is dividing by 1, and the highest divisor we can use is the max of nums, so everything will divide to 1

        left = 1
        right = max(nums)

        while left <= right:
            mid = (left + right) // 2
            sum_val = sum(math.ceil(num / mid) for num in nums)
            if sum_val <= threshold:  # We want to divide by a smaller num
                right = mid - 1
            else:
                left = mid + 1
            # Left will stop at the lowest divisor that makes sum_val <= threshold
        return left
