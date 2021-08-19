class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        (left, right) = (1, max(nums))
        while left < right:
            mid = left + (right - left) // 2
            divided = sum([num // mid + int(num % mid > 0) for num in nums])
            if divided > threshold:
                left = mid + 1
            else:
                right = mid
        return right
