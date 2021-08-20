class Solution:

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return sum(nums)
        elif len(nums) == 3:
            return sum(nums)
        nums = sorted(nums)
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                if s < target:
                    j += 1
                else:
                    k -= 1
                if abs(s - target) < abs(res - target):
                    res = s
        return res
