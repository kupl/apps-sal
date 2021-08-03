from collections import defaultdict, Counter


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = defaultdict(lambda: defaultdict(lambda: 1))
        best = 0
        for i in range(len(A)):
            num = A[i]

            for prev_num in list(dp.keys()):
                step = num - prev_num
                dp[num][step] = max(dp[prev_num][step] + 1, dp[num][step])
                best = max(best, dp[num][step])
            dp[num][0] = max(dp[num][0], 1)
            best = max(dp[num][0], best)
        return best
