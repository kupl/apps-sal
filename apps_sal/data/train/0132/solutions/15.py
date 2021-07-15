class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf') for d in range(days[-1]+1)]
        dp[0] = 0
        pass_num_days = [1, 7, 30]
        days_set = set(days)
        
        for day in range(days[-1]+1):
            if day not in days_set:
                dp[day] = dp[max(0, day-1)]
            else:
                for num_days, cost in zip(pass_num_days, costs):
                    dp[day] = min(dp[day], dp[max(0, day-num_days)] + cost)
        print(dp)
        return dp[-1]    
