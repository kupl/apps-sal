import math


def rec(coins, amount, used_coins, res):
    if amount == 0:
        res[0] = min(res[0], used_coins)
    elif coins and (res[0] - used_coins) * coins[-1] >= amount:
        for i in range(amount // coins[-1], -1, -1):
            rec(coins[:-1], amount - i * coins[-1], used_coins + i, res)


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [math.inf]
        rec(sorted(coins), amount, 0, res)
        return res[0] if res[0] != math.inf else -1
