class Solution:

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        dp[0] = 0
        for j in range(len(days)):
            i = days[j]
            for k in range(1, i + 1):
                if k == i:
                    if k - 7 >= 0 and k - 30 >= 0:
                        dp[k] = min(dp[k - 1] + costs[0], dp[k - 7] + costs[1], dp[k - 30] + costs[2])
                    elif k - 7 >= 0:
                        dp[k] = min(dp[k - 1] + costs[0], dp[k - 7] + costs[1], costs[2])
                    else:
                        dp[k] = min(dp[k - 1] + costs[0], costs[1], costs[2])
                elif k != 1:
                    if dp[k] == 0:
                        dp[k] = dp[k - 1]
        return dp[-1]
