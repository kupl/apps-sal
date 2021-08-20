class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        if K == 1:
            return sum(A) / len(A)
        memo = [[0] * len(A) for _ in range(K)]
        cumsum = [0] * len(A)
        for i in range(len(A)):
            cumsum[i] = cumsum[i - 1] + A[i]
            memo[0][i] = cumsum[i] / (i + 1)
        for i in range(1, K):
            for j in range(i, len(A)):
                tmp = 0
                for k in range(i - 1, j):
                    tmp = max(tmp, memo[i - 1][k] + (cumsum[j] - cumsum[k]) / (j - k))
                memo[i][j] = tmp
        return memo[-1][-1]
