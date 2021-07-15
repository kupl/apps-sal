class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def solve(i,j,arr,dp):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            
            op1 = arr[i]+solve(i+1,j,arr,dp)
            op2 = arr[j]+solve(i,j-1,arr,dp)
            dp[i][j] = max(op1,op2)
            return dp[i][j]
        dp = [[-1]*500]*500
        ans = solve(0,len(piles)-1,piles,dp)
        ans2 = sum(piles)-ans
        return ans>ans2

