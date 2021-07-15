from collections import defaultdict
class Solution:
    
    def longestArithSeqLength(self, A: List[int]) -> int:
        def gen():
            x = [0 for i in range(l)]
            x[0] = 1
            return x
        
        # dp[diff][index]
        l = len(A)
        dp = defaultdict(lambda: [1 for i in range(l)])
        ans = 0
        for i in range(l):
            for j in range(i+1, l):
                dp[A[j]-A[i]][j] = dp[A[j]-A[i]][i] + 1
                ans = max(ans,dp[A[j]-A[i]][j] )

            
        return ans
        

