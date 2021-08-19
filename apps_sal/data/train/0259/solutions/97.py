"""
Binary search to find the best divisor that doesn't go through the threshold
"""


class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def ok(divisor):
            sol = 0
            for n in nums:
                sol += ceil(n / divisor)
            return sol <= threshold
        lo = 1
        hi = max(nums)
        while lo <= hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
