class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        c = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] <= c[0]:
                c[0] = nums[i]
                continue

            if nums[i] > c[-1]:
                c.append(nums[i])
                continue

            l = 0
            h = len(c) - 1

            while l + 1 != h:
                m = (l + h) >> 1
                if nums[i] > c[m]:
                    l = m
                else:
                    h = m
            c[h] = nums[i]

        return len(c)
