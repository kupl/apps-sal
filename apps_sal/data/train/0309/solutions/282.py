class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = [{} for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                step = A[i] - A[j]
                dp[i][step] = max(dp[i].get(step, 0), dp[j].get(step, 1) + 1)
        return max((max(dp[i].values(), default=0) for i in range(n)))
