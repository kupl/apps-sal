class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = defaultdict(int)
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i, diff] = dp[j, diff] + 1
        return max(dp.values()) + 1
