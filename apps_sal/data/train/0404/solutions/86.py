class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        if not A:
            return 0
        elif len(A) <= K:
            return sum(A)
        size = len(A)
        dp = [[0] * (size + 1) for _ in range(K + 1)]
        for j in range(size):
            dp[1][j + 1] = sum(A[:j + 1]) / (j + 1)
        for k in range(2, K + 1):
            for i in range(k, size + 1):
                suffixSum = 0
                for j in range(i, k - 1, -1):
                    suffixSum += A[j - 1]
                    dp[k][i] = max(dp[k][i], dp[k - 1][j - 1] + suffixSum / (i - j + 1))
        print(dp)
        return max([dp[i][size] for i in range(1, K + 1)])
