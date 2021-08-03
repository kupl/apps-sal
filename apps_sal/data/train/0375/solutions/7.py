class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math
        import sys
        if not nums or len(nums) < 2:
            return 0

        lenn = len(nums)
        maxx = nums[0]
        minn = nums[0]
        for i in range(len(nums)):
            maxx = max(maxx, nums[i])
            minn = min(minn, nums[i])

        gap = math.ceil((maxx - minn) / (lenn - 1))
        bucketsMin = [2**31 - 1] * (lenn - 1)
        bucketsMax = [-2**31 + 1] * (lenn - 1)
        for num in nums:
            if num == minn or num == maxx:
                continue
            bucket = (num - minn) // gap
            bucketsMin[bucket] = min(num, bucketsMin[bucket])
            bucketsMax[bucket] = max(num, bucketsMax[bucket])
        res = 0
        pre = minn
        for i in range(lenn - 1):
            if bucketsMin[i] == (2**31 - 1) and bucketsMax[i] == (-2**31 + 1):
                continue
            res = max(res, bucketsMin[i] - pre)
            pre = bucketsMax[i]

        res = max(res, maxx - pre)
        return res
