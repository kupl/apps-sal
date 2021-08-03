class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        Cum = [0]
        for i in range(len(A)):
            Cum.append(Cum[-1] + A[i])

        def Average(h, k):
            return (Cum[k] - Cum[h]) / (k - h)

        dp = [Average(i, len(A)) for i in range(len(A))]
        for _ in range(K - 1):
            for i in range(len(A)):
                for j in range(i + 1, len(A)):
                    dp[i] = max(dp[i], Average(i, j) + dp[j])
        return dp[0]
