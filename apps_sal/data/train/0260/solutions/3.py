class Solution:

    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        max_up = [1]
        max_down = [1]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                max_up.append(max_down[i - 1] + 1)
                max_down.append(max_down[i - 1])
            elif nums[i] < nums[i - 1]:
                max_up.append(max_up[i - 1])
                max_down.append(max_up[i - 1] + 1)
            else:
                max_up.append(max_up[i - 1])
                max_down.append(max_down[i - 1])
        return max(max_up[-1], max_down[-1])
