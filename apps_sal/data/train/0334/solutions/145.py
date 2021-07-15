class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        
        s = list(s)
        v = 0
        i = 0
        while i < len(s)-1:
            if s[i] == s[i+1]:
                v += min(cost[i],cost[i+1])   
                cost[i+1] = max(cost[i],cost[i+1])
            i += 1
            
        return v
