class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        N = len(A)
        dp = defaultdict(lambda: 1)
        for j in range(N):
            dp2 = defaultdict(lambda: 1)
            for i in range(j):
                (y, z) = (A[i], A[j])
                d = delta = z - y
                dp2[z, d] = max(dp2[z, d], dp[y, d] + 1)
            dp.update(dp2)
        return max(dp.values())
