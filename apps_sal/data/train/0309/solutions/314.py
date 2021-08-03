class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i, a1 in enumerate(A):
            for j, a2 in enumerate(A[:i]):
                diff = a1 - a2
                if (j, diff) in dp:
                    dp[i, diff] = 1 + dp[j, diff]
                else:
                    dp[i, diff] = 2
        return max(dp.values())
