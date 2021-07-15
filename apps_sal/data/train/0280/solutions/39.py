class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n=len(s)
        palindrome=[[0 for x in range(n)] for y in range(n)]
        for i in range(n-1):
            if s[i]!=s[i+1]:
                palindrome[i][i+1]=1
        for gap in range(2,n):
            for start in range(n-gap):
                end=start+gap
                if s[start]==s[end]:
                    palindrome[start][end]=palindrome[start+1][end-1]
                else:
                    palindrome[start][end]=palindrome[start+1][end-1]+1
        dp=[[2**31 for x in range(k+1)] for y in range(n+1)]
        dp[0][0]=0
        for i in range(1,n+1):
            for j in range(1,k+1):
                for l in range(i,0,-1):
                    dp[i][j]=min(dp[i][j],dp[l-1][j-1]+palindrome[l-1][i-1])
        return dp[n][k]
                    

