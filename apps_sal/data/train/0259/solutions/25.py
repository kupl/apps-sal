class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left <= right:
            mid = (right + left) // 2
            acc = 0
            for n in nums:
                acc += math.ceil(n / mid)
            if acc > threshold:
                left = mid + 1
            elif acc <= threshold:
                right = mid - 1
        return left
