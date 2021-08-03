class Solution(object):
    def twoSum(self, nums, target):
        """ 
        :type nums: List[int] 
        :type target: int 
        :rtype: List[int] 
        """
        arr = {}
        length = len(nums)
        for i in range(length):
            if (target - nums[i]) in arr:
                return [arr[target - nums[i]], i]
            arr[nums[i]] = i
