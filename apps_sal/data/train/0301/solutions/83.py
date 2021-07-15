class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = collections.defaultdict(int)
        m = len(A)
        n = len(B)
        
        for i in range(m):
            for j in range(n):
                dp[i,j] = max(dp[i-1,j], dp[i,j-1], dp[i-1,j-1] + (A[i] == B[j]))
        return dp[m-1,n-1]
