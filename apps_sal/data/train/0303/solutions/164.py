class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        
        n = len(A)
        dp = [0] * (n+1)
        for i in range(1,n+1):
            j = i - 1
            mx = -float('inf')
            while i - j <= K and j >= 0:
                mx = max(mx,A[j])
                dp[i] = max(dp[i],dp[j]+mx * (i - j))
                j -= 1
        return dp[n]


