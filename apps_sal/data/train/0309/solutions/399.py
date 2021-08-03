class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = defaultdict(int)

        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                d = A[j] - A[i]

                if (i, d) in dp:
                    dp[j, d] = dp[i, d] + 1
                else:
                    dp[j, d] = 2

        return max(dp.values())
