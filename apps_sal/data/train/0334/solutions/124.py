class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        
        res = 0
        i = 1
        N = len(s)
        
        while i < N:
            if s[i] == s[i-1]:
                maxcost = cost[i-1]
                totalcost = cost[i-1]
                while i < N and s[i] == s[i-1]:
                    totalcost += cost[i]
                    maxcost = max(maxcost, cost[i])
                    i += 1
                    
                print(totalcost, maxcost)
                res += (totalcost - maxcost)
                
            i += 1
            
        return res
