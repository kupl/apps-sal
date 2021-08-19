class Solution:

    def twoSum(self, nums, target):
        tmp = {}
        for i in range(len(nums)):
            if target - nums[i] in tmp:
                return (tmp[target - nums[i]], i)
            else:
                tmp[nums[i]] = i
        '\n         :type nums: List[int]\n         :type target: int\n         :rtype: List[int]\n         '
