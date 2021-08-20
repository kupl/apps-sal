class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:

        def avg(array):
            return sum(array) / len(array)
        dp = [[0 for _ in range(K)] for _ in range(len(A))]
        dp[0][0] = A[0]
        for i in range(len(A)):
            for j in range(K):
                if j == 0:
                    dp[i][j] = avg(A[:i + 1])
                else:
                    for k in range(i):
                        dp[i][j] = max(dp[i][j], dp[k][j - 1] + avg(A[k + 1:i + 1]))
        return dp[len(A) - 1][K - 1]
