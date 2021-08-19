class Solution:

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 2:
            return list(set(nums))
        (can, can2) = (0, 0)
        (num, num2) = (0, 1)
        for i in range(len(nums)):
            if nums[i] == can:
                num += 1
            elif nums[i] == can2:
                num2 += 2
            elif num == 0:
                num = 1
                can = nums[i]
            elif num2 == 0:
                num2 = 1
                can2 = nums[i]
            else:
                (num, num2) = (num - 1, num2 - 1)
        res = []
        if nums.count(can) > int(len(nums) / 3):
            res.append(can)
        if nums.count(can2) > int(len(nums) / 3) and can2 != can:
            res.append(can2)
        return res
