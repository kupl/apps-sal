class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A)<=2:
            return len(A)
        
        dp = [{} for _ in range(len(A))]
        dp[1][A[1]-A[0]] = 2
        
        maxLen = 0
        for i in range(2, len(A)):
            for j in range(i):
                diff = A[i]-A[j]
                dp[i][diff] = max(dp[i][diff] if diff in dp[i] else 0, dp[j][diff]+1 if diff in dp[j] else 2)
                maxLen = max(maxLen, dp[i][diff])
        
        return maxLen
