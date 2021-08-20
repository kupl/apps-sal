class Solution:

    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def checkv(t, c, nums, used):
            if t == 0:
                return True
            if t < 0:
                return False
            while c < len(nums) and used[c]:
                c = c + 1
            if c >= len(nums):
                return False
            if checkv(t - nums[c], c + 1, nums, used):
                used[c] = True
                return True
            if checkv(t, c + 1, nums, used):
                return True
            return False
        edgel = sum(nums)
        if edgel % 4 != 0 or edgel == 0:
            return False
        edgel = edgel / 4
        nums.sort(key=lambda x: -x)
        n = len(nums)
        used = [False] * n
        for p in range(3):
            t = edgel
            if not checkv(t, 0, nums, used):
                return False
        return True
