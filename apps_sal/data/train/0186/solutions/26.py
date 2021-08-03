class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [0] + [-1] * (target + 5000)
        for t in range(1, target + 1):
            p = []
            for i, c in enumerate(cost):
                p.append(dp[t - c] * 10 + i + 1)
                dp[t] = max(p)
        return str(max(dp[t], 0))
