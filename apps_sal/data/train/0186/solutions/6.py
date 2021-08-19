class Solution:

    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [float('-inf')] * (target + 1)
        dp[0] = 0
        for i in range(1, 10):
            for j in range(1, target + 1):
                c = cost[9 - i]
                if c <= j:
                    dp[j] = max(dp[j - c] * 10 + (10 - i), dp[j])
        return str(dp[target]) if str(dp[target]) != '-inf' else '0'
