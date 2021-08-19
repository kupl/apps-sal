class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        curr_max = nums[0]
        curr_min = nums[0]
        sub_nums = []
        for num in nums:
            if abs(num - curr_max) <= limit and abs(num - curr_min) <= limit and (abs(curr_max - curr_min) <= limit):
                curr_max = max(num, curr_max)
                curr_min = min(num, curr_min)
                sub_nums.append(num)
            else:
                sub_nums.append(num)
                sub_nums.pop(0)
                curr_max = max(sub_nums)
                curr_min = min(sub_nums)
        return len(sub_nums)
