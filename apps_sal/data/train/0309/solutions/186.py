class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        dp = dict()
        for i in range(n):
            for j in range(i + 1, n):
                d = nums[j] - nums[i]
                if (i, d) in list(dp.keys()):
                    dp[(j, d)] = dp[(i, d)] + 1
                else:
                    dp[(j, d)] = 2
        return max(dp.values())
