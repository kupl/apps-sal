class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [0, 0, 0]

        for i, x in enumerate(nums):
            m = x % 3
            if i > 0:
                rot = [dp[(x - m) % 3] for x in range(3)]

                for j in range(3):
                    if rot[j] > 0:
                        dp[j] = max(dp[j], rot[j] + x)

            dp[m] = max(dp[m], x)

        return dp[0]
