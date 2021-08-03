class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        dp = ['0'] * n
        for i in range(1, n):
            dp[i] = dp[i - 1] + '1' + ''.join([str(1 - int(n)) for n in dp[i - 1]])[::-1]
        return dp[-1][k - 1]
