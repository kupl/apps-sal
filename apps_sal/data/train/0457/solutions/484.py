class Solution:
    def changeCoin(self, coins, amount, change):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if amount in change:
            return change[amount]

        costs = []

        for coin in coins:
            cost = self.changeCoin(coins, amount - coin, change)
            if amount - coin in change:
                change[amount - coin] = min(cost, change[amount - coin])
            else:
                change[amount - coin] = cost

            if cost != -1:
                costs.append(cost)

        if len(costs) == 0:
            return -1

        return 1 + min(costs)

    def coinChange(self, coins: List[int], amount: int) -> int:

        change = {}

        return self.changeCoin(coins, amount, change)
