class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [[-1 for _ in range(amount + 1)] for _ in coins]
        for i in range(len(coins) - 1, -1, -1):
            for j in range(amount + 1):
                if j == 0:
                    memo[i][j] = 0
                    continue
                if j - coins[i] >= 0 and memo[i][j - coins[i]] != -1 and (i + 1 < len(coins)) and (memo[i + 1][j] != -1):
                    memo[i][j] = min(memo[i][j - coins[i]] + 1, memo[i + 1][j])
                elif j - coins[i] >= 0 and memo[i][j - coins[i]] != -1:
                    memo[i][j] = memo[i][j - coins[i]] + 1
                elif i + 1 < len(coins) and memo[i + 1][j] != -1:
                    memo[i][j] = memo[i + 1][j]
        return memo[0][amount]
