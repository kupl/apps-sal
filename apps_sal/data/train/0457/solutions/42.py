class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        store = [float('inf')] * (amount + 1)
        store[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0 and store[i] > store[i - coin] + 1:
                    store[i] = store[i - coin] + 1
        return store[amount] if store[amount] != float('inf') else -1
