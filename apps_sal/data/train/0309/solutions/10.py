class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        
        dp = [{} for _ in range(n)]
        
        ans = 0
        
        for i in range(n):
            dp[i][0] = 1
            for j in range(i):
                diff = A[i] - A[j]
                
                if diff not in dp[j]:
                    dp[i][diff] = 2
                else:
                    dp[i][diff] = dp[j][diff] + 1
            
            ans = max(ans, max([dp[i][key] for key in dp[i]]))
        
        return ans
