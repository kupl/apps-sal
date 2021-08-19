class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = []
        res = 0
        for i in range(len(A)):
            step2len = defaultdict(int)
            dp.append(step2len)
            for prev_i in range(i):
                step = A[i] - A[prev_i]
                prev_step = dp[prev_i][step]
                dp[i][step] = prev_step + 1
                res = max(res, dp[i][step])
        return res + 1
