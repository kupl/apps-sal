class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # binary search
        left = 1
        right = max(nums)
        while left <= right:
            mid = left + (right - left) // 2
            mid_left_result = self.divide_and_sum(mid - 1, nums)
            mid_result = self.divide_and_sum(mid, nums)
            if mid_left_result > threshold and mid_result <= threshold:
                return mid
            # move right
            if mid_result > threshold:
                left = mid + 1
            # move left
            if mid_left_result <= threshold:
                right = mid - 1

    def divide_and_sum(self, divisor, nums):
        if divisor == 0:
            return math.inf

        result = 0
        for num in nums:
            result += ceil(num / divisor)

        return result
