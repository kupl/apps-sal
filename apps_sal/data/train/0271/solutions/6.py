class Solution:

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        res = [False for num in nums]
        res[0] = True
        end = 0
        for (i, num) in enumerate(nums):
            if res[i] == False:
                continue
            if i + num >= len(nums):
                return True
            if end < i + num:
                for j in range(end + 1, i + num + 1):
                    res[j] = True
                end = i + num
        return res[-1]
