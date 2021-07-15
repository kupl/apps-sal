class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        ans = 2
        n = len(A)
        index = {}
        dp = [[2] * n for i in range(n)]
        
        for i in range(n-1):
            for j in range(i+1, n):
                first = A[i] * 2 - A[j]
                if first in index:
                    dp[i][j] = dp[index[first]][i] + 1
                    ans = max(ans, dp[i][j])
            index[A[i]] = i
        return ans
