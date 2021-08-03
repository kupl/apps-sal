class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def condition(mid):
            sum_nums = 0
            for num in nums:
                sum_nums += ceil(num / mid)
            return sum_nums <= threshold

        left = 1
        right = max(nums)
        while left < right:
            mid = (left + right) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
