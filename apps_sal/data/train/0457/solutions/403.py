import math


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1

        if amount == 0:
            return 0

        memo = [0] * amount

        def findNumCoins(remainingAmount: int) -> int:
            nonlocal memo

            if remainingAmount < 0:
                return -1
            if remainingAmount == 0:
                return 0
            memo_idx = remainingAmount - 1
            if memo[memo_idx] != 0:
                return memo[memo_idx]

            local_min = math.inf
            for coin in coins:
                res = findNumCoins(remainingAmount - coin)
                if res >= 0:
                    local_min = min(local_min, 1 + res)
            num_coins = -1 if local_min == math.inf else local_min
            memo[memo_idx] = num_coins
            return num_coins

        return findNumCoins(amount)
