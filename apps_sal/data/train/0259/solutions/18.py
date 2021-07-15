class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        #print(math.ceil(7/3))
        high = sum(nums)
        if high <= threshold: return 1
        
        def sum_divide(divisor):
            su = 0
            for num in nums:
                su += math.ceil(num / divisor)
                if su > threshold:
                    return False
            return True    
        
        low = 1
        while low < high:
            mid = low + (high - low) // 2
            if sum_divide(mid):
                high = mid
            else:
                low = mid + 1
                
        return low       

