class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i = 0
        j = 0
        max_length = 1
        cur_max = cur_min = nums[0]
        while j < len(nums):
            dif = cur_max - cur_min
            if dif <= limit:
                max_length = j-i+1
                j += 1
                if j < len(nums):
                    cur_max = max(cur_max,nums[j])
                    cur_min = min(cur_min,nums[j])
            else:
                i += 1
                j += 1
                cur_max = max(nums[i:j+1])
                cur_min = min(nums[i:j+1])
        return max_length
