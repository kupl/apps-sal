class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        
        n = len(A)
        
        # 2 4 6
        # 2 1 4 6
        # 2 3 4 6 8
        
        increment = 0
        num_steps = 0
        dp = {}
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                diff = A[j] - A[i]
                
                if (i,diff) not in dp:
                    dp[j,diff] = 2
                else:
                    dp[j,diff] = dp[i,diff] + 1
        
        return max(dp.values())
            
            
                
                
            
            

