class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        import itertools
        cumsum = list(itertools.accumulate(A))
        L = len(A)
        K = min(L, K)
        dp = [[0] * (K + 1) for i in range(L)]
        for i in range(L):
            dp[i][1] = (cumsum[i]) / (i + 1)
        for k in range(2, K + 1):
            for i in range(L):
                tmp = dp[i][k - 1]
                for j in range(i):
                    tmp = max(tmp, dp[j][k - 1] + (cumsum[i] - cumsum[j]) / (i - j))
                dp[i][k] = tmp
        return dp[-1][K]
