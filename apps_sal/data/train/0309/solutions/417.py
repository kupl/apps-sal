class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        N = len(A)
        dp = defaultdict(lambda: 1)
        for j in range(N):
            nxt = defaultdict(lambda: 1)
            for i in range(j):
                y, z = A[i], A[j]
                d = delta = z - y
                nxt[z, d] = max(nxt[z, d], dp[y, d] + 1)
            dp.update(nxt)
        return max(dp.values())
