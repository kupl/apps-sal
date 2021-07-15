class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        def helper(n,k):
            if (n,k) in dp: return dp[n,k]
            if k==1: return sum(A[:n])/n
            if n<=k: return sum(A[:n])
            dp[n,k],temp = 0,0
            for i in range(1,n)[::-1]:
                temp+=A[i]
                dp[n,k]=max(dp[n,k],helper(i,k-1)+temp/(n-i))
            return dp[n,k]
            
        dp = {}
        return helper(len(A),K)
