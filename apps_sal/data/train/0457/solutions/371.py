class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp_table = [float('inf')] * (amount + 1)
        dp_table[0] = 0
        return self.dp(dp_table, coins, amount)

    def dp(self, dp_table: [float], coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if dp_table[amount] != float('inf'):
            return dp_table[amount]
        res = float('inf')
        for coin in coins:
            subpb = self.dp(dp_table, coins, amount - coin)
            if subpb == -1:
                continue
            res = min(res, subpb + 1)
        dp_table[amount] = res if res != float('inf') else -1
        return dp_table[amount]
