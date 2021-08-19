class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        res = curr = 0
        dp = {0: 0}
        for (i, num) in enumerate(nums, 1):
            if num == 0:
                curr = 0
                dp = {0: i}
                continue
            curr = (curr + (num < 0)) % 2
            if curr not in dp:
                dp[curr] = i
            else:
                res = max(res, i - dp[curr])
        return res
