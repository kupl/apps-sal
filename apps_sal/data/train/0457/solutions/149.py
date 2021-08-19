class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [amount + 1] * (amount + 1)
        table[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    table[i] = min(table[i - coin] + 1, table[i])
        print(table)
        return table[amount] if table[amount] != amount + 1 else -1
