class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        x = coinCount(coins, amount, {})
        if x == float('inf'):
            return -1
        return x


def coinCount(coins, amount, found):
    if amount < 0:
        return float('inf')
    if amount == 0:
        return 0
    if found.get(amount):
        return found[amount]
    count = 0
    minCount = float('inf')
    for coin in coins:
        if coin == amount:
            return 1
        count = 1 + coinCount(coins, amount - coin, found)
        if count < minCount:
            minCount = count
    found[amount] = minCount
    return minCount
