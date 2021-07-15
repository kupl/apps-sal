class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = list(dict() for i in range(len(A)))
        maxsize = 0
        for i in range(1,len(A)):
            for j in range(0,i):
                diff = A[j] - A[i]
                if(diff in dp[j]):
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 1
            
                maxsize = max(maxsize, dp[i][diff])
        
        return maxsize + 1

