class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if self.findSum(nums, mid) > threshold:
                left = mid + 1
            else:
                right = mid
        return left
    
    
    def findSum(self, nums, divisor):
        return sum(math.ceil(num / divisor) for num in nums)
