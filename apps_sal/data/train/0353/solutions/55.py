MD = 10 ** 9 + 7

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        if nums is None or not nums:
            return 0
        
        N = len(nums)
        
        nums.sort()
        
        start = 0
        end = N - 1
        
        ret = len([d for d in nums if d + d <= target])
        
        while start < end:
            while start < end and nums[start] + nums[end] > target:
                end -= 1
                
            if start < end:
                ret = (ret + self.fast_pow(2, MD, end - start) - 1) % MD
                start += 1
                
        return ret
    
    def fast_pow(self, a, md, n):
        if n == 0:
            return 1 % md
        
        if n == 1:
            return a % md
        
        ret = self.fast_pow(a, md, n // 2)
        ret = (ret * ret ) % md
        
        if n % 2 == 1:
            ret = (ret * a) % md
        
        return ret

