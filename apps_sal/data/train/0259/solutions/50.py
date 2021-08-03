from math import ceil


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            d = (l + r) // 2
            s = sum([ceil(n / d) for n in nums])
            if s > threshold:
                l = d + 1
            else:
                r = d
        return l
