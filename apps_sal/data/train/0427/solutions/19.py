class Solution:
    def countOrders(self, n: int) -> int:
        DP = [0] * (n + 1)
        DP[1] = 1
        for i in range(2, n + 1):
            newpos = ((i * 2 - 1) + 1) * (i * 2 - 1) // 2
            DP[i] = newpos * DP[i - 1]

        return DP[-1] % (10**9 + 7)
