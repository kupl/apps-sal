class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        dic = {}

        def score(i, j, t):
            if i > j:
                return 0
            if (i, j) in dic:
                return dic[(i, j)]
            ret = max(t - score(i + 1, j, t - nums[i]), t - score(i, j - 1, t - nums[j]))
            dic[(i, j)] = ret
            return ret
        l = len(nums)
        sc = score(0, l - 1, total)
        return sc >= total - sc
