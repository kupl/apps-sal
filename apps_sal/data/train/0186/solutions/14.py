class Solution:

    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [0] + [-1] * target
        for i in range(1, target + 1):
            for (j, c) in enumerate(cost):
                if c <= i:
                    dp[i] = max(dp[i], dp[i - c] * 10 + j + 1)
        return str(max(dp[target], 0))
