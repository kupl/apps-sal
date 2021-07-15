class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        n1 = len(A)
        n2 = len(B)
        dp = [[-1 for _ in range(n2)] for _ in range(n1)]
        return self.recur(0,0,A,B,n1,n2, dp)
    
    def recur(self,i,j,A,B,n1,n2,dp):
        if i == n1 or j == n2:
            return 0
        
        
        if dp[i][j] != -1:
            return dp[i][j]
        if A[i] == B[j]:
            dp[i][j] =  1 + self.recur(i+1,j+1,A,B,n1,n2,dp)
        else:
            c1 = self.recur(i+1,j,A,B,n1,n2,dp)
            c2 = self.recur(i,j+1,A,B,n1,n2,dp)
            dp[i][j] = max(c1,c2)
            
        return dp[i][j]
            

