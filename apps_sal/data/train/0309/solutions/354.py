class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = []
        maximum = 1
        for i in range(len(A)):
            d = {}
            dp.append({})
            for j in range(i):
                diff = A[i]-A[j]
                if(diff not in dp[i]):
                    dp[i][diff] = 0
                if(diff not in dp[j]):
                    dp[j][diff] = 0
                dp[i][diff] = dp[j][diff]+1
                maximum = max(maximum,dp[i][diff])
        
        return maximum+1
