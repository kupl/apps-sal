class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = collections.defaultdict(int)
        for i in range(0, len(A)):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                if (i, diff) in dp:
                    dp[j, diff] = dp[i, diff] + 1
                else:
                    dp[j, diff] = 2
        return max(dp.values())
