import math 
class Solution: 
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # bruteforce 
        '''
        divisor = 0 
        trial_sum = float(inf) 
        while trial_sum > threshold:
            divisor += 1 
            trial_sum = 0 
            for num in nums: 
                trial_sum += math.ceil(num / divisor)
           

        return divisor 
        '''
        
        # binary search 
        low = 1 
        high = 100000000
        while (low <= high):
            mid = low + (high - low) // 2 
            if self.getSum(nums, mid) <= threshold: 
                high = mid - 1 
            elif self.getSum(nums, mid) > threshold: 
                low = mid + 1 
        return low
    def getSum(self, nums, divisor):
        trial_sum = 0 
        for num in nums: 
            trial_sum += math.ceil(num / divisor)
        return trial_sum 
    
    
            
    
            
        

