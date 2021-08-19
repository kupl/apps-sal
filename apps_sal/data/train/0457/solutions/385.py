import math


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # want fewest number of coins to form the amount
        if amount == 0:
            return 0
        records = [-2] * amount
        return helper(amount, coins, records)


def helper(amount, coins, records):
    # base
    if amount == 0:
        return 0
    if amount < 0:
        return -1

    # recursive function, iterate, top-down
    if records[amount - 1] != -2:
        min_number = records[amount - 1]
    else:
        min_number = math.inf
        for c in coins:
            val = helper(amount - c, coins, records)
            if val != -1:
                val += 1
                min_number = min(val, min_number)
#                records[amount - 1] = min_number
    if min_number == math.inf:
        records[amount - 1] = -1
        return -1
    else:
        records[amount - 1] = min_number
        return min_number
