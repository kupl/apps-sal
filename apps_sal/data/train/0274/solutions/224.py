class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums: return 0
        if len(nums) == 1: return 1
        
        l, r = 0, 1
        cur_mx, cur_mi = nums[0], nums[0]
        
        max_l = 1
        
        while l <= r and r < len(nums):
            cur_mx = max(cur_mx, nums[r])
            cur_mi = min(cur_mi, nums[r])
            
            if cur_mx - cur_mi <= limit:
                max_l = max(max_l, r - l + 1)
                r += 1
            else:
                cur_mx = max(nums[l+1: r+1])
                cur_mi = min(nums[l+1: r+1])
                r += 1
                l += 1
        
        return max_l
                

