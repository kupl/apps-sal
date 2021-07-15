class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        i=0
        res=0
        j = 1
        while j<len(s):
            if s[i]==s[j]:
                res+=min(cost[i],cost[j])
                cost[j]=max(cost[i],cost[j])
            i+=1
            j+=1
        return res
