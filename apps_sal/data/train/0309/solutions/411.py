class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = defaultdict(lambda: 1)
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i, diff] = 1 + dp[j, diff]
        return max(dp.values())
