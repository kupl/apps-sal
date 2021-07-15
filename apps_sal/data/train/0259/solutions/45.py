class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        
        while l < r:
            
            m = (l + r) // 2
            
            if sum((n + m - 1) // m for n in nums) > threshold:
                l = m + 1
            else:
                r = m
                
        return l
