import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if not nums:
            return sys.maxsize
        left, right = 1, 2
        while right < sys.maxsize and self.get_sum(nums, right) > threshold:
            left, right = right, right * 10

        
        while left + 1 < right:
            mid = (left + right) // 2
            if self.get_sum(nums, mid) <= threshold:
                right = mid
            else:
                left = mid
        if self.get_sum(nums, left) <= threshold:
            return left
        return right
    
    def get_sum(self, nums: List[int], divisor: int) -> int:
        result = 0
        for num in nums:
            result += math.ceil(num / divisor)
        return int(result)
