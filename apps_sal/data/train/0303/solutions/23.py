class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        dp = [0] * (n + 1)
        for i, a in enumerate(A):
            r = a
            for j in range(1, K + 1):
                r = max(r, A[i - j + 1] if i - j + 1 >= 0 else float('-inf'))
                # print(i, j, r, dp)
                if i - j + 1 >= 0:
                    dp[i + 1] = max(dp[i + 1], dp[i - j + 1] + r * j)
        return dp[-1]
