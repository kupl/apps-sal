class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        pos = 0

        for i in range(1, days[-1] + 1):
            if i == days[pos]:
                d1 = i - 1
                d2 = i - 7 if i - 7 > 0 else 0
                d3 = i - 30 if i - 30 > 0 else 0
                dp[i] = min(dp[d1] + costs[0], dp[d2] + costs[1], dp[d3] + costs[2])
                pos += 1
            else:
                dp[i] = dp[i - 1]

        return dp[-1]
