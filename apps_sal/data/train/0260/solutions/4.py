class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = len(nums)
        dp = [0] * l
        up = [0] * l
        down = [0] * l
        up[0] = down[0] = 1
        for i in range(1, l):
            if nums[i - 1] < nums[i]:
                up[i] = up[i - 1]
                down[i] = up[i - 1] + 1
            elif nums[i - 1] > nums[i]:
                down[i] = down[i - 1]
                up[i] = down[i - 1] + 1
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]
        return max(down[-1], up[-1])
