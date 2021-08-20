class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        N = len(A)
        index = {n: i for (i, n) in enumerate(A)}
        dp = collections.defaultdict(lambda: 2)
        res = 0
        for i2 in range(N):
            for i1 in range(i2 - 1, -1, -1):
                n0 = A[i2] - A[i1]
                if n0 >= A[i1]:
                    break
                if n0 in index:
                    i0 = index[n0]
                    dp[i1, i2] = dp[i0, i1] + 1
                    res = max(res, dp[i1, i2])
        return res
