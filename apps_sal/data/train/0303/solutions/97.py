class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [0]
        for i in range(len(A)):
            curr = 0
            for j in range(i, max(-1, i - K), -1):
                curr = max(max(A[j:i + 1]) * (i - j + 1) + dp[j], curr)
            dp.append(curr)
        print(dp)
        return dp[-1]
