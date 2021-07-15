class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        f = [[float('inf')] * (amount + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(amount + 1):
                f[i][j] = f[i - 1][j]
                if coins[i - 1] <= j:
                    f[i][j] = min(f[i][j], 1 + f[i][j - coins[i - 1]])
        return f[n][amount] if f[n][amount] != float('inf') else -1
