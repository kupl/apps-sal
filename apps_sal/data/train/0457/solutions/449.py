class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [float('inf') for _ in range(amount + 1)]
        i = 0
        table[0] = 0
        for coin in coins:
            if coin <= amount:
                table[coin] = 1
        while i <= amount:
            for coin in coins:
                if i - coin >= 0:
                    table[i] = min(table[i - coin] + 1, table[i])
            i += 1
        return table[amount] if table[amount] != float('inf') else -1
