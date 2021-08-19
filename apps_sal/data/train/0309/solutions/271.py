class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = defaultdict(dict)
        n = len(A)
        best = 0
        for i in range(1, n):
            for j in range(0, i):
                de = A[i] - A[j]
                dp[i][de] = dp[j].get(de, 1) + 1
                best = max(best, dp[i][de])
        return best
