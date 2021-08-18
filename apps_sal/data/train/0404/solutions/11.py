import itertools


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        P = [0] + list(itertools.accumulate(A))
        def average(i, j): return (P[j] - P[i]) / float(j - i)

        N = len(A)
        dp = [average(i, N) for i in range(N)]
        for _ in range(K - 1):
            for i in range(N):
                for j in range(i + 1, N):
                    dp[i] = max(dp[i], average(i, j) + dp[j])

        return dp[0]
