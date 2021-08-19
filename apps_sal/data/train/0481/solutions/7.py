class Solution:

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] > target + abs(result - target):
                return result
            st = i + 1
            ed = len(nums) - 1
            while st < ed:
                dis = nums[i] + nums[st] + nums[ed] - target
                if dis == 0:
                    return target
                elif dis > 0:
                    while st < ed and nums[i] + nums[st] + nums[ed] - target > 0:
                        ed -= 1
                    if abs(nums[i] + nums[st] + nums[ed + 1] - target) < abs(result - target):
                        result = nums[i] + nums[st] + nums[ed + 1]
                else:
                    while st < ed and nums[i] + nums[st] + nums[ed] - target < 0:
                        st += 1
                    if abs(nums[i] + nums[st - 1] + nums[ed] - target) < abs(result - target):
                        result = nums[i] + nums[st - 1] + nums[ed]
        return result
