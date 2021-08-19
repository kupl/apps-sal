class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        cur_max = nums[0]
        cur_min = nums[0]
        sub_nums = []  # 以数组作为窗口滑动
        for i in nums:
            cur_max = max(i, cur_max)
            cur_min = min(i, cur_min)
            if cur_max - cur_min <= limit:
                sub_nums.append(i)
            else:
                sub_nums.append(i)
                sub_nums.pop(0)
                cur_max = max(sub_nums)
                cur_min = min(sub_nums)
        return len(sub_nums)
