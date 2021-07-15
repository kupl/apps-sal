class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        n = len(A)
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                d = A[j] - A[i]
                dp[j, d] = dp.get((i, d), 1) + 1
                ans = max(ans, dp[j, d])
        
        return ans
