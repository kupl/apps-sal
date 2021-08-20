class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = []
        m = 0
        for (i, a) in enumerate(A):
            dp.append(defaultdict(int))
            for j in range(i):
                dif = a - A[j]
                dp[i][dif] = dp[j][dif] + 1
                m = max(m, dp[i][dif])
        return m + 1
