class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        
        n = len(A)
        if n < 3: return n
        
        dp = [{} for _ in range(n)]
        max_ = 0
        for i in range(1, n):
            for j in range(i):
                
                diff = A[i] - A[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                
                max_ = max(max_, dp[i][diff])
        
        return max_

