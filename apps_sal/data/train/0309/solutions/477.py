class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        ans = 0
        dp = {}
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                j1 = (j , diff)
                i1 = (i, diff)
                if dp.get(j1) != None:
                    dp[i1] = 1 + dp[j1]
                    ans = max(ans, dp[i1])
                else:
                    dp[i1] = 2
                    ans = max(ans, dp[i1])

        return ans
            
                    
                

