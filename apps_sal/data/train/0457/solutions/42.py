class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     if amount == 0:
    #         return 0
    #     coins.sort(reverse = True)
    #     m = amount + 1
    #     store = [float('inf')] * m
    #     store[0] = 0
    #     for i in range(len(coins)):
    #         x = self.countChange(coins, amount, i, store)
    #         if x > -1:
    #             m = min(m, x)
    #     return m if m != amount + 1 else -1

    def coinChange(self, coins: List[int], amount: int) -> int:

        store = [float('inf')] * (amount + 1)
        store[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0 and store[i] > store[i - coin] + 1:
                    store[i] = store[i - coin] + 1
        return store[amount] if store[amount] != float('inf') else -1

    # def countChange(self, coins: List[int], amount: int, index: int, store) -> int:
    #     if amount == 0:
    #         return 0
    #     elif store[amount] != float('inf'):
    #         return store[amount]
    #     elif index >= len(coins):
    #         return -1
    #     elif amount < coins[index]:
    #         return -1
    #     m = float('inf')
    #     for i in range(1, amount // coins[index] + 1):
    #         for j in range(len(coins)+1):
    #             x = self.countChange(coins, amount - coins[index] * i, j, store)
    #             if x > -1:
    #                 m = min(m, x + i)
    #     store[amount] = m
    #     return m if m != float('inf') else -1

    # def countChange(self, coins: List[int], amount: int, index: int) -> int:
    #     if index >= len(coins):
    #         return 0
    #     elif amount < coins[index]:
    #         return 0
    #     # num = amount // coins[index]
    #     num = 1
    #     print(coins, amount, index, num)
    #     amount -= coins[index]
    #     if amount == 0:
    #         return num
    #     for i in range(index, len(coins)):
    #         x = self.countChange(coins, amount, i)
    #         if x > 0:
    #             return x + num
    #     else:
    #         return 0
