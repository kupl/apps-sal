class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = defaultdict(lambda: 1)
        n = len(A)
        for i in range(n):
            for j in range(i):
                dp[i, A[i] - A[j]] = max(dp[i, A[i] - A[j]], dp[j, A[i] - A[j]] + 1)
        return max(dp.values())
