class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        
        while left < right:
            mid = left + (right-left)//2
            
            total = sum([(x + mid - 1)//mid for x in nums])
            
            if total > threshold:
                left = mid + 1
            else:
                right = mid
                
        return left

