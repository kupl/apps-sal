class Solution:
    # Time: O(n)
    # Space: O(n)
    def longestSubarray(self, nums: List[int]) -> int:
        right = [0 for _ in range(len(nums))]
        left = [0 for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            if nums[i - 1]:
                left[i] = 1 + left[i - 1]
             
        for i in range(len(nums) - 2, -1, -1):
            if nums[i + 1]:
                right[i] = 1 + right[i + 1]
            
        res = float('-inf')
        for i in range(len(nums)):
            res = max(res, left[i] + right[i])
        return res
