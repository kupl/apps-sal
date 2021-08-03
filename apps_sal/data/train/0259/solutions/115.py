class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def feasible(val):
            total = 0
            for i in nums:
                total += (i - 1) // val + 1
            return total <= threshold

        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left
