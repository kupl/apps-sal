class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        i=0
        ans=0
        while i<len(s):
            if i<len(s)-1 and s[i]==s[i+1]:
                n=0
                t=i
                temp=s[i]
                while i<len(s) and s[i]==temp:
                    i+=1
                    n+=1
                #print(n, s, cost, cost[t:t+n], sum(cost[t:t+n]), max(cost[t:t+n]))
                ans+=(sum(cost[t:t+n])-max(cost[t:t+n]))
            else:
                i+=1
        return ans

