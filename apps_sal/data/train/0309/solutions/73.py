class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A: return 0
        if len(A)<3: return 2
        dp = {}
        for i, a1 in enumerate(A[1:], 1):
            for j, a2 in enumerate(A[:i]):
                diff = a1 - a2
                if (j, diff) in dp:
                    dp[i, diff] = dp[j, diff] + 1
                else:
                    dp[i, diff] = 2
                    
        return max(dp.values())
                
            
        
        
        
                        

