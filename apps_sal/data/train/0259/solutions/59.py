from numpy import array, ceil, sum
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums = array(nums)
        l, r = 1, max(nums)
        while l < r:
            mid = (l+r)//2
            if sum(ceil(nums / mid)) <= threshold:
                r = mid
            else:
                l = mid + 1
        return r   
        
        
        
        
        
        

