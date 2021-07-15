class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        
        left, right = 0, len(nums)-1
        
        ans = 0
        mod = 10**9+7
        while left<right:
            if nums[left] + nums[right] > target:
                right -= 1
                continue
            else:
                ans = (ans + 2**(right-left)-1) % mod
                left += 1
            
        
        for n in nums:
            if n*2<=target:
                ans += 1
        
        return ans%mod
