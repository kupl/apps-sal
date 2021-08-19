class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        # tnums = tuple(nums)
        # move to the solve function

        def solve(nums):
            # BUG！ IndexError: list index out of range
            if len(nums) <= 1:
                return sum(nums)
            tnums = tuple(nums)
            if tnums in dic:
                return dic[tnums]
            dic[tnums] = max(nums[0] - solve(nums[1:]), nums[-1] - solve(nums[:-1]))
            # TypeError: unsupported operand type(s) for -: 'int' and 'NoneType'
            return dic[tnums]
        return solve(nums) >= 0
