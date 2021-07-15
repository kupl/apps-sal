from numpy import array, ceil, sum
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        ''' Original solution
        def div(a,b):
            return (a//b + 1 - (a//b == a/b))
        
        divisor = max(nums)//2
        divided_list = [div(num, divisor) for num in nums]
        
        left = 1
        right = max(nums)
        while right - left > 1:
            
            goleft = (sum(divided_list) <= threshold)
            
            if goleft:
                right = divisor
                divisor = (divisor + left) // 2
                
            else:
                left = divisor
                divisor = (divisor + right) // 2
            
            #print(f\"left:{left}, right:{right}\")
            
            divided_list = [div(num, divisor) for num in nums]

        if sum(divided_list) > threshold:
            divisor += 1
        
        return divisor'''
        
        nums = array(nums)
        l, r = int(ceil(sum(nums)/threshold)), max(nums)
        
        while l < r:
            mid = (l+r)//2
            if sum(ceil(nums/mid)) <= threshold:
                r = mid
            else:
                l = mid + 1
        
        return r
