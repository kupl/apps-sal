class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A:
            return 0
        n = len(A)
        dp = [{} for i in range(n)]
        ans = 0
        for i in range(1, n):
            for j in range(i):
                diff = A[i] - A[j]
                tmp = dp[j].get(diff, 0)
                dp[i][diff] = tmp + 1
                ans = max(ans, tmp+1)
        return ans+1
                    
                    
        

