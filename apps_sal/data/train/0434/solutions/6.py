class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_length = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
                max_length = max(max_length, count)
            else:
                count = 0
        
        if max_length == len(nums):
            return len(nums) - 1
        elif max_length == 0:
            return 0
        
        num_left = 0
        num_right = 0
        for i, num in enumerate(nums):
            if num == 1:
                num_right += 1
            else:
                max_length = max(max_length, num_left + num_right)
                if i + 1 < len(nums) and nums[i + 1] == 1:
                    num_left = num_right
                    num_right = 0
                else:
                    num_left = 0
                    num_right = 0
        max_length = max(max_length, num_left + num_right)
        
        return max_length
