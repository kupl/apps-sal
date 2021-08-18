class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        if not A:
            return 0
        dp = {}
        averages = [[None] * len(A) for _ in range(len(A))]
        for i in range(len(A)):
            averages[i][i] = A[i]
            for j in range(i + 1, len(A)):
                averages[i][j] = (averages[i][j - 1] * (j - i) + A[j]) / (j - i + 1)

        def recurse(A, K, start):
            if start >= len(A):
                return 0
            if K == 1:
                return averages[start][len(A) - 1]
            if (K, start) in dp:
                return dp[K, start]
            dp[K, start] = -math.inf
            for i in range(start, len(A)):
                dp[K, start] = max(dp[K, start], averages[start][i] + recurse(A, K - 1, i + 1))
            return dp[K, start]
        return recurse(A, K, 0)
