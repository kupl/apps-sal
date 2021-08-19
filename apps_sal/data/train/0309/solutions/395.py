class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                curr_diff = A[j] - A[i]
                dp[j, curr_diff] = dp.get((i, curr_diff), 1) + 1
        return max(dp.values())
