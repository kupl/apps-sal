class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        i = 1
        current_cost = cost[0]
        max_cost = cost[0]
        ans = 0
        while i < len(cost):
            while i < len(cost) and s[i] == s[i-1]:
                current_cost += cost[i]
                max_cost = max(max_cost, cost[i])
                i += 1
                
            ans += current_cost - max_cost
            
            if i < len(cost):
                current_cost = cost[i]
                max_cost = cost[i]
            
            i += 1
            
        return ans
