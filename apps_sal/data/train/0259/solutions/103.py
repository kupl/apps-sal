class Solution:
    
    def check(self,divisor,nums,threshold):
        result = 0
        for number in nums:
            k = int(number/divisor)
            if number % divisor != 0:
                k +=1
            result += k
            if result > threshold:
                return False
        return True
        
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        while low <= high:
            mid = int((low+high)/2)
            if self.check(mid,nums,threshold):
                high = mid -1
            else:
                low = mid+1
        return low

