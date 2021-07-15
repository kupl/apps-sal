class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        curr_max = nums[0] # 当子数组下最大值 这里初始化为第一个数
        curr_min = nums[0] # 当子数组下最大值 这里初始化为第一个数
        sub_nums = [] # 以数组作为窗口滑动
        for num in nums:
            if abs(num - curr_max) <=  limit and abs(num - curr_min) <=  limit and abs(curr_max - curr_min) <= limit:
                curr_max = max(num,curr_max)
                curr_min = min(num,curr_min)
                sub_nums.append(num)
            else: #缩小窗口   
                sub_nums.append(num)#先append 当前数
                sub_nums.pop(0)#移除最左边
                curr_max = max(sub_nums) # 更新最值
                curr_min = min(sub_nums)
        return  len(sub_nums)


