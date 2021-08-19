class Solution:

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        maxReachable = 0
        for (i, num) in enumerate(nums):
            if num >= n - i - 1:
                return True
            flag = False
            if i + num >= maxReachable:
                for j in range(i + 1, num + i + 1):
                    if nums[j] > 0:
                        flag = True
                        break
                if flag == False:
                    return False
            maxReachable = max(maxReachable, i + num)
        return True
