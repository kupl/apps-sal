class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A:
            return 0
        
        dp = [{} for _ in range(len(A))]
                
        max_seq = 1
        
        for i in range(1, len(A)):
            dp[i] = {0:1}
            
            for j in range(i):
                diff = A[i] - A[j]
                
                if diff not in dp[j]:
                    dp[i][diff] = 2
                else:
                    dp[i][diff] = dp[j][diff] + 1
                
                max_seq = max(max_seq, dp[i][diff])
                        
        return max_seq
            
                
                
            
        

