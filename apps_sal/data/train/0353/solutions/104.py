class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        N = len(nums)
        nums.sort()
        ans =  0
        l, r = 0, N-1
        
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                ans += 2**(r-l)
                l += 1
        
        return ans % (10**9 + 7)
