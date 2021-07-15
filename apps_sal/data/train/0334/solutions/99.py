class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        s=list(s)
        ret=0
        i=1
        while i<len(s):
            if s[i]==s[i-1]:
                ret+=min(cost[i],cost[i-1])
                if cost[i]<cost[i-1]:
                    
                    cost[i],cost[i-1]=cost[i-1],cost[i]
            i+=1
        return ret
