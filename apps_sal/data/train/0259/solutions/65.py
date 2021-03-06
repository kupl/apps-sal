class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        (L, R) = (1, max(nums) + 1)

        def solve(divisor):
            sums = 0
            for num in nums:
                sums += num // divisor
                sums += 0 if num % divisor == 0 else 1
            return sums > threshold
        while L < R:
            mid = L + (R - L) // 2
            if solve(mid):
                L = mid + 1
            else:
                R = mid
        return R
