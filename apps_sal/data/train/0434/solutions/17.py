class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        joined = [0 for i in range(n)]
        # downto = [0 for i in range(n)]
        left = 0
        right = 0
        for i in range(n):
            joined[i] += left
            joined[n - 1 - i] += right
            if nums[i] == 1:
                left += 1
            else:
                left = 0
            if nums[n - 1 - i] == 1:
                right += 1
            else:
                right = 0
        
        return max(joined)
