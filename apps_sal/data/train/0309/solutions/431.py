class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = [{} for i in range(n)]
        result = 0
        for i, a in enumerate(A):
            for j in range(i):
                l = dp[j].get(a - A[j], 1) + 1
                dp[i][a - A[j]] = max(dp[i].get(a - A[j], 0), l)
                result = max(result, l)
        return result
