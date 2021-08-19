class Solution:

    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        gn = [1] * n
        trend = 0
        for i in range(1, n):
            prev = nums[i - 1]
            if prev == nums[i]:
                gn[i] = gn[i - 1]
            else:
                if trend == 0:
                    gn[i] = gn[i - 1] + 1
                    trend = 1 if nums[i] > prev else -1
                    continue
                if nums[i] > prev and trend == -1 or (nums[i] < prev and trend == 1):
                    gn[i] = gn[i - 1] + 1
                    trend = -trend
                else:
                    gn[i] = gn[i - 1]
        return gn[-1]
