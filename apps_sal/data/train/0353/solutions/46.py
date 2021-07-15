class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        
        ans = 0
        
        for i in range(len(nums)):
            
            if 2 * nums[i] <= target:
                ans += 1
                
            lo, hi = i + 1, len(nums) - 1
            
            while lo < hi:
                m = (lo + hi) // 2 + 1
                
                if nums[i] + nums[m] > target:
                    hi = m - 1
                else:
                    lo = m

            if nums[i] + nums[hi] <= target:
                ans += (1 << (hi - i)) - 1
                
        return ans % (10 ** 9 + 7)
