class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        L = len(A)
        dp = [[0 for _ in range(K + 1)] for _out in range(L)]
        prefix_sum = [0 for _ in range(L + 1)]
        for i in range(1, L + 1):
            prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]
        dp[0][1] = A[0]
        for i in range(1, L):
            dp[i][1] = (prefix_sum[i] + A[i]) / (i + 1)
        for i in range(1, L):
            for k in range(2, K + 1):
                if k > i + 1:
                    dp[i][k] = dp[i][k - 1]
                else:
                    for j in range(-1, i):
                        subarr = A[j + 1:i + 1]
                        ave = (prefix_sum[i + 1] - prefix_sum[j + 1]) / (i - j)
                        if j == -1:
                            tmp = 0
                        else:
                            tmp = dp[j][k - 1]
                        if ave + tmp > dp[i][k]:
                            dp[i][k] = ave + tmp
        return dp[-1][-1]
