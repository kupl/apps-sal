class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        len_A = len(A)
        dp = [[0 if j else sum(A[:i + 1]) / (i + 1) for j in range(K)] for i in range(len_A)]
        for i in range(len_A):
            for j in range(1, K):
                if j > i:
                    break
                for k in range(i):
                    dp[i][j] = max(dp[i][j], dp[k][j - 1] + sum(A[k + 1:i + 1]) / (i - k))
        return dp[-1][-1]
