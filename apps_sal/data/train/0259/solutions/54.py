from math import ceil


class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        def cal_sum(div):
            div_sum = 0
            for num in nums:
                div_sum += ceil(num / div)
            return div_sum
        while left < right:
            mid = left + (right - left) // 2
            if cal_sum(mid) > threshold:
                left = mid + 1
            else:
                right = mid
        return right
