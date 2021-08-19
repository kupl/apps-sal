import math


def rec(coins, amount, used_coins, res):
    if amount == 0:
        res[0] = min(res[0], used_coins)
    elif coins:
        (coin, rest_coins) = (coins[-1], coins[:-1])
        for i in range(amount // coin, -1, -1):
            if (res[0] - used_coins) * coin >= amount:
                rec(rest_coins, amount - i * coin, used_coins + i, res)


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [math.inf]
        rec(sorted(coins), amount, 0, res)
        return res[0] if res[0] != math.inf else -1
