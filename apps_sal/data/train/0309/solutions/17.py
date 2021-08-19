class Solution:

    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 2:
            return n
        dp = [{} for i in range(n)]
        res = 0
        for i in range(1, n):
            for j in range(i):
                dis = nums[i] - nums[j]
                x = dp[j].get(dis, 1) + 1
                dp[i][dis] = x
            res = max(res, max(dp[i].values()))
        return res
