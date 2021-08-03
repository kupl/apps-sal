class Solution:
    def countOrders(self, n: int) -> int:

        dp = [1 for i in range(n)]

        for i in range(1, n):
            sequence = i + 1
            length = 2 * (i)
            temp = sum([j for j in range(1, length + 2)])
            dp[i] = temp * dp[i - 1]

        print(dp)
        return dp[-1] % (10**9 + 7)
