class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [[-1 for i in range(n+1)] for i in range(10)]
        d={1:[6,8],2:[7,9],3:[4,8],4:[3,9,0],5:[],6:[1,7,0],7:[2,6],8:[1,3],9:[2,4],0:[4,6]}
        out = 0
        for i in range(0,10):
            out+=self.helper(n-1,i,d,dp)
        return out%1000000007
    
    def helper(self,n,index,d,dp):
        if(n==0):
            return 1
        
        if(dp[index][n]!=-1):
            return dp[index][n]
        
        ans = 0
        for i in range(len(d[index])):
            ans+=self.helper(n-1,d[index][i],d,dp)
        dp[index][n] = ans
        return ans
