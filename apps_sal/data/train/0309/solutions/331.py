class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        from collections import defaultdict
        dp = [Counter() for _ in range(len(A))]
        
        
        max_length = 0
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                # Was this difference earlier seen at index j? Then continue that chain
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else: # If no, create a new chain of length 2
                    dp[i][diff] = 2
                    
                max_length = max(max_length, dp[i][diff])
        # Print this table for any input for better understanding of the approach
        # print table

        return max_length
        
    

