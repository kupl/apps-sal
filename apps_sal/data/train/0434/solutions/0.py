class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if not 0 in nums:
            return len(nums) - 1
        ans = 0
        tot = 0
        prev = 0
        
        for n in nums:
            if n == 1:
                tot += 1
            else:
                ans = max(tot+prev, ans)
                prev = tot
                tot = 0
        return max(prev+tot, ans)
                

