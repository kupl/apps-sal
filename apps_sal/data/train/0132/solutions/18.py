class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        if not days: 
            return 0
        lastday = days[-1]
        
        dp = [0] * (lastday + 1)
        
        for i in range(1, lastday + 1): 
            if i not in days: 
                dp[i] = dp[i - 1]
                continue
            prev_1 = dp[i - 1] if i >= 1 else 0
            prev_7 = dp[i - 7] if i >= 7 else 0
            prev_30 = dp[i - 30] if i >= 30 else 0
            dp[i] = min(prev_1 + costs[0], prev_7 + costs[1], prev_30 + costs[2])
        
        return dp[-1]
            

