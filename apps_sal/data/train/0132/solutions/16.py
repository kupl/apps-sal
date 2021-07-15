class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        given = {}
        for day in days:
            given[day] = True
        
        dp = [0 for _ in range(days[-1]+1)]
        dp[1] = costs[0]
        for day in range(days[-1]+1):
            if day not in given:
                dp[day] = dp[day-1]
            else:
                # purchase one day pass
                one_day_pass = dp[max(0, day-1)] + costs[0]
                # purchase one week pass
                one_week_pass = dp[max(0, day-7)] + costs[1]
                # purchase one month pass
                one_month_pass = dp[max(0,day-30)] + costs[2]
                dp[day] = min(one_day_pass, one_week_pass, one_month_pass)
        print(dp)
        return dp[-1]
