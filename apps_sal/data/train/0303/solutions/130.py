class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:

        dp = [0 for _ in A]

        for i, num in enumerate(A):
            for j in range(K):
                ans = 0
                if i - j >= 0:
                    ans = ans + (j + 1) * max(A[i - j:i + 1])
                if i - j - 1 >= 0:
                    ans = ans + dp[i - j - 1]
                dp[i] = max(dp[i], ans)

        return dp[-1]
