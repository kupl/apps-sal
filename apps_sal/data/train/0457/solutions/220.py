import math


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        counts = [0] * amount
        return f(coins, amount, counts)


def f(coins, amount, counts):
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    if counts[amount - 1] != 0:
        return counts[amount - 1]
    min_val = math.inf
    for c in coins:
        res = f(coins, amount - c, counts)
        if res >= 0 and res < min_val:
            min_val = 1 + res
    if min_val == math.inf:
        counts[amount - 1] = -1
    else:
        counts[amount - 1] = min_val
    return counts[amount - 1]
