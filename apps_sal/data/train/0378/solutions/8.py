class Solution:

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = sum(nums)
        if target % 2 == 1:
            return False
        target = target // 2
        if any([x for x in nums if x > target]):
            return False
        nums.sort()

        def check(nums, target):
            if target in nums:
                return True
            if not nums or nums[0] > target:
                return False
            res = False
            tag = '@'
            for i in range(len(nums)):
                if tag != nums[i]:
                    tag = nums[i]
                    res = res | check(nums[:i] + nums[i + 1:], target - nums[i])
                    if res:
                        return True
            return res
        return check(nums, target)
