class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # dp[i][k] = longestArithSeqLength(A[:i+1]) with step size k
        largest = max(A)
        smallest = min(A)

        dp = dict()
        res = 0

        for i in range(1, len(A)):
            for prev_i in range(i):
                step = A[i] - A[prev_i]
                prev_step = dp[(prev_i, step)] if (prev_i, step) in dp else 1
                if (i, step) not in dp:
                    dp[(i, step)] = prev_step + 1
                else:
                    dp[(i, step)] = max(prev_step + 1, dp[(i, step)])

                res = max(res, dp[(i, step)])

        return res
