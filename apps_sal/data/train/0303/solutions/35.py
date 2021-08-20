class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [0] * len(A)
        for i in range(K):
            dp[i] = (i + 1) * max(A[:i + 1])
        for i in range(K, len(A)):
            maximum = 0
            for j in range(1, K + 1):
                if i - j < 0:
                    break
                temp = dp[i - j] + max(A[i - j + 1:i + 1]) * j
                if temp > maximum:
                    maximum = temp
            dp[i] = maximum
        print(dp)
        return dp[-1]
