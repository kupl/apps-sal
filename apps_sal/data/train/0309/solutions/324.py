class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = defaultdict(int)
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                span = A[i] - A[j]
                dp[j, span] = dp.get((i, span), 1) + 1
        return max(dp.values())
