class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        
        if len(A) < 3:
            return len(A)
        
        dp = [ {} for i in range(len(A))]
        m = 2
        
        for i in range(1, len(A)):
            for j in range(i):  # here we have to iterate from 0 to i-1 and not i-1 to 0.
                
                diff = A[i] - A[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff]+1
                    if m < dp[i][diff]:
                        m = dp[i][diff]
                else:
                    dp[i][diff] = 2

        return m
                
                
                
                
                
                
                
                
                
                

