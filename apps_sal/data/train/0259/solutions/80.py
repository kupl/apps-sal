class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        n = len(nums)
        while low < high:
            mid = low + (high - low) // 2
            s = 0
            for i in range(n):
                s += math.ceil(nums[i] / mid)
            if s > threshold:
                low = mid + 1
            else:
                high = mid
        return high
