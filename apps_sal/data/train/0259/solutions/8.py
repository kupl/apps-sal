class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        # if the sum <= threshold, the divisor is big enough
        
        low, high = 1, max(nums)
        
        while low < high:
            mid = (low + high) // 2
        
            # if the sum > threshold, the divisor is too small
            if sum((i + mid - 1) // mid for i in nums) > threshold:
                low = mid + 1
            else:
                high = mid
                
        return low

