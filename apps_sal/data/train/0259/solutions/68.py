import numpy as np

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        nums = np.array(nums)
        left = sum(nums) // threshold
        right = max(nums) + 1
        
        while left < right:
            mid = left + (right - left) // 2

            if np.sum(np.ceil(nums / mid)) <= threshold:
                right = mid
            else:
                left = mid + 1
        return left
        

