class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        mcost=0
        i=0
        c=0
        j=0
        while(i<len(s)):
            j=i
            while(i<len(s) and s[j]==s[i]):
                i+=1
                c+=1
            if(c!=1):
                mcost+=sum(cost[j:i])-max(cost[j:i])
            c=0
        return mcost
