class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        dp = {}
        def a(n,k):
            if n<k:return 0
            if (n,k) in dp:return dp[n,k]
            if k == 1:
                dp[n,k] = sum(A[:n])/float(n)
                return dp[n,k]
            dp[n,k] = 0
            for i in range(n-1,0,-1):
                a(i,k-1)
                dp[n,k] = max(dp[n,k],a(i,k-1) + sum(A[i:n])/float(n-i))
        a(len(A),K)
        return dp[len(A),K]
