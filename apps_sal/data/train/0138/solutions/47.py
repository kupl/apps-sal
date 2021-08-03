class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        dp = [0 for _ in range(2)]
        res = 0

        if nums[0] > 0:
            dp[0] = 1
            res = 1
        if nums[0] < 0:
            dp[1] = 1

        for i in range(1, len(nums)):
            cur = nums[i]
            tmp = [0 for _ in range(2)]
            if cur > 0:
                tmp[0] = dp[0] + 1
                if dp[1] > 0:
                    tmp[1] = dp[1] + 1

            if cur < 0:
                tmp[1] = dp[0] + 1
                if dp[1] > 0:
                    tmp[0] = dp[1] + 1

            res = max(res, tmp[0])
            dp = tmp

        return res
