import sys
class Solution:
    def rec(self,l,h,cuts,dp):
        if h in dp[l]:
            return dp[l][h] 
        ans=sys.maxsize
        for i in cuts:
            if l<i and i<h:
                if i in dp[l]:
                    k1=dp[l][i]
                else:
                    k1=self.rec(l,i,cuts,dp)
                if h in dp[i]:
                    k2=dp[i][h]
                else:
                    k2=self.rec(i,h,cuts,dp)
                ans=min(ans,h-l+k1+k2)
        if ans==sys.maxsize:
            ans=0
        dp[l][h]=ans
        return dp[l][h]
                
    def minCost(self, n: int, cuts: List[int]) -> int:
        dp={}
        for i in range(n+1):
            dp[i]={}
        return self.rec(0,n,cuts,dp)

