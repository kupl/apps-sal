class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        dp = [[0.0 for j in range(K + 1)] for i in range(len(A))]
        sums = [0] * len(A)
        sums[0] = A[0]
        for i in range(1, len(A)):
            sums[i] = sums[i - 1] + A[i]
        for k in range(1, K + 1):
            for i in range(len(A)):
                if k == 1:
                    dp[i][k] = sums[i] / (i + 1)
                elif k > i + 1:
                    continue
                else:
                    for j in range(k - 1, i + 1):
                        avg1 = dp[j - 1][k - 1]
                        avg2 = (sums[i] - sums[j - 1]) / (i - j + 1)
                        if dp[i][k] < avg1 + avg2:
                            dp[i][k] = avg1 + avg2
        return dp[-1][K]
