class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums or limit < 0:
            return 0
        anchor = ans = 0
        (hi, lo) = (float('-inf'), float('inf'))
        for i in range(len(nums)):
            hi = max(hi, nums[i])
            lo = min(lo, nums[i])
            if hi - lo <= limit:
                ans = max(ans, i - anchor + 1)
            else:
                if nums[anchor] == hi:
                    hi = max(nums[anchor + 1:i + 1])
                elif nums[anchor] == lo:
                    lo = min(nums[anchor + 1:i + 1])
                anchor += 1
        return ans
