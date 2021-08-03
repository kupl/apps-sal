from bisect import bisect_left


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        hi = math.ceil(len(nums) * max(nums) / threshold)
        lo = math.ceil(sum(nums) / threshold)

        while lo <= hi:
            med = (lo + hi) // 2
            cur = self.divSum(nums, med)
            if cur <= threshold:
                hi = med - 1
            else:
                lo = med + 1

        return lo

    def divSum(self, nums, div):
        total = 0
        for num in nums:
            total += math.ceil(num / div)
        return total
