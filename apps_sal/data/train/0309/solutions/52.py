class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [defaultdict(int) for a in A]
        for (i, a) in enumerate(A):
            for j in range(i):
                dp[i][a - A[j]] = dp[j][a - A[j]] + 1
        m = 0
        for d in dp:
            x = d.values()
            if x:
                m = max(m, max(x))
        return m + 1
