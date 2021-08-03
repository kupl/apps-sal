class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0

        h = {}
        dp = []
        s = nums[0]
        if s == target:
            dp.append(1)
        else:
            dp.append(0)
        h[s] = 0
        for i in range(1, len(nums)):
            s = s + nums[i]
            if s == target:
                if 0 in h:
                    dp.append(max(dp[h[0]] + 1, dp[-1]))
                else:
                    dp.append(max(1, dp[-1]))
            elif s - target in h:
                dp.append(max(dp[h[s - target]] + 1, dp[-1]))
            else:
                dp.append(dp[-1])
            h[s] = i
        return dp[-1]
