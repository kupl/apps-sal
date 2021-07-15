MOD = 10 ** 9 + 7

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        N = len(nums)
        if N == 1:
            return 1 if nums[0] * 2 <= target else 0
        
        nums.sort()
        
        ret = 0
        start = 0
        end = N - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] * 2 > target:
                end = mid
            else:
                start = mid
                
        if nums[end] * 2 > target:
            if nums[start] * 2 > target:
                return 0
            ret += end
        else:
            return (2 ** (end + 1) - 1) % MOD
        
        start = 0
        end = N - 1
        
        while start < end:
            if nums[start] + nums[end] > target:
                end -= 1
                continue
                
            ret = (ret + 2 ** (end - start) - 1) % MOD
            start += 1
            
        return ret
        

