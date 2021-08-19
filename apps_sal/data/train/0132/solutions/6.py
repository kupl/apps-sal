class Solution:

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        for day in range(0, days[-1] + 1):
            if day not in days:
                dp[day] = dp[max(0, day - 1)]
            else:
                dp[day] = min(dp[max(0, day - 1)] + costs[0], dp[max(0, day - 7)] + costs[1], dp[max(0, day - 30)] + costs[2])
        return dp[-1]
