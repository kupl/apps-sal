class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        M = [[0 for j in range(amount + 1)] for i in range(len(coins) + 1)]
        for j in range(1, amount + 1):
            M[0][j] = 1000000
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    M[i][j] = min(1 + M[i][j - coins[i - 1]], M[i - 1][j])
                else:
                    M[i][j] = M[i - 1][j]
        return M[-1][-1] if M[-1][-1] < 1000000 else -1
