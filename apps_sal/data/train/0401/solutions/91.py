class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [[0] * len(nums) for _ in range(3)]
        for (i, n) in enumerate(nums):
            if i == 0:
                dp[n % 3][0] = n
            else:
                for rem in range(3):
                    if dp[rem][i - 1] % 3 == rem:
                        dp[(n + rem) % 3][i] = max(dp[rem][i - 1] + n, dp[(n + rem) % 3][i - 1])
                    else:
                        dp[(n + rem) % 3][i] = dp[(n + rem) % 3][i - 1]
        return dp[0][-1] if dp[0][-1] != float('-inf') else 0
