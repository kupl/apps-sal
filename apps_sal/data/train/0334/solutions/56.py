class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if(len(s)<=1):
            return 0
        
        prev=0
        cost_val = 0
        for i in range(1,len(s)):
            if(s[i]==s[prev]):
                if(cost[i]<=cost[prev]):
                    cost_val+=cost[i]
                else:
                    cost_val+=cost[prev]
                    prev=i
            else:
                prev=i

        return cost_val
