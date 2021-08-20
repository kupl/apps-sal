class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = collections.defaultdict(int)
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i, diff] = max(2, dp[j, diff] + 1)
        return max(dp.values())
