class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}

        def solve(nums):
            if len(nums) <= 1:
                return sum(nums)
            tnums = tuple(nums)
            if tnums in dic:
                return dic[tnums]
            dic[tnums] = max(nums[0] - solve(nums[1:]), nums[-1] - solve(nums[:-1]))
            return dic[tnums]
        return solve(nums) >= 0
