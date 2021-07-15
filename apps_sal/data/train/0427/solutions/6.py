class Solution:
    def countOrders(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        mod = 10 ** 9 + 7
        for i in range(2, n+1):
            spaces = (i-1) * 2 + 1
            permutations = sum(j for j in range(1, spaces+1))
            dp[i] = (dp[i-1] * permutations) % mod
        return dp[n]
