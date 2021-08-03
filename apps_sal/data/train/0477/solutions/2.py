class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        dp = [[]] * n
        dp[0] = [0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + [1] + list(reversed([v ^ 1 for v in dp[i - 1]]))
        return str(dp[-1][k - 1])
