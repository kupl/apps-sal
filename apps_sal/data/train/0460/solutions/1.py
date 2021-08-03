class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen = 0
        for i in range(0, len(nums)):
            cur = nums[i]
            if(cur >= 0):
                curlen = 0
                nums[i] = -1
                while cur >= 0:
                    j = cur
                    cur = nums[j]
                    nums[j] = -1
                    curlen = curlen + 1
                if curlen > maxlen:
                    maxlen = curlen
        return maxlen
