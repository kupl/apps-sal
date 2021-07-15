import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        small, big = 1, max(nums)
        while small < big:
            mid = small + (big-small)//2
            cur = 0
            for num in nums:
                cur += math.ceil(num/mid)
            if cur > threshold:
                small = mid + 1
            else:
                big = mid
        return small
