import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)
        while low < high:
            mid = (low+high)//2
            if sum(math.ceil(num/mid) for num in nums) > threshold:
                low = mid + 1
            else:
                high = mid
        return low

