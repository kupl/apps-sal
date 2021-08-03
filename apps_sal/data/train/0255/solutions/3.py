class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = [0]
        for i in range(len(nums) - 1):
            while(i + nums[i] >= len(p) and len(p) < len(nums)):
                p.append(p[i] + 1)
        return p[-1]
