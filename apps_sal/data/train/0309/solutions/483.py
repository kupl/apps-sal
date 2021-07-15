class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [{} for _ in range(len(A))]
        max_len = 0
        for i in range(len(A)-1):
            
            for j in range(i+1, len(A)):
                diff = A[j] - A[i]
                
                if dp[i].get(diff) == None:
                    dp[j][diff] = 2
                else:
                    dp[j][diff] = dp[i][diff] + 1
                max_len = max(dp[j][diff], max_len)
                
        return max_len
