class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf')] * (len(days) + 1)
        dp[0] = 0
        for i in range(1, len(days) + 1):
            j = 0
            while i + j < len(dp):
                if days[i + j - 1] <= days[i - 1]:
                    dp[i + j] = min(dp[i + j], dp[i - 1] + costs[0])
                if days[i + j - 1] <= days[i - 1] + 6:
                    dp[i + j] = min(dp[i + j], dp[i - 1] + costs[1])
                if days[i + j - 1] <= days[i - 1] + 29:
                    dp[i + j] = min(dp[i + j], dp[i - 1] + costs[2])
                else:
                    break
                j += 1
        return dp[-1]

