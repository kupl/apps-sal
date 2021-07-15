class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = max(nums)
        
        if d==0:
            return 0
        
        res = 0
        while d>=2:
            res += 1
            d >>= 1
            

        for num in nums:
            while num:
                res += 1
                num &= (num-1)
            
        return res

