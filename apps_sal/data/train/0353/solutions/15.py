class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        l,r = 0, n-1
        counts = 0
        res = 0
        
        while True:
            while l<=r and nums[r]+nums[l]>target:
                r -= 1
            if l<=r:
                res += pow(2, (r-l), 10**9+7)
                res %= 10**9 + 7
                l += 1
            else:
                break
            
        return res 

