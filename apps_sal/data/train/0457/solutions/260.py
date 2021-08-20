class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        memory = {}
        return self._helper(coins, amount, memory)

    def _helper(self, coins, amount, memory):
        if amount < 0:
            return -1
        elif amount == 0:
            return 0
        elif amount in memory:
            return memory[amount]
        potential_values = []
        for coin in coins:
            new_target = amount - coin
            min_coins = self._helper(coins, new_target, memory)
            if min_coins != -1:
                potential_values.append(min_coins)
        if len(potential_values) == 0:
            memory[amount] = -1
        else:
            memory[amount] = min(potential_values) + 1
        return memory[amount]
