class Solution:

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        a = 1
        b = n
        while a < b:
            m = (a + b) // 2
            lCount = 0
            hCount = 0
            for k in nums:
                if a <= k <= m:
                    lCount += 1
                elif m < k <= b:
                    hCount += 1
            if lCount > m - a + 1:
                b = m
            else:
                a = m + 1
        return a
