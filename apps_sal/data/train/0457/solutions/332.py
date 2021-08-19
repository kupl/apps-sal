from collections import defaultdict


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        def coin_change_for_amount(coins, amount):
            nonlocal count_amount
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            if count_amount[amount] != float('inf'):
                return count_amount[amount]
            min_coins_amt = float('inf')
            for coin in coins:
                min_coins_amt_coin = coin_change_for_amount(coins, amount - coin)
                if 0 <= min_coins_amt_coin < min_coins_amt:
                    min_coins_amt = min_coins_amt_coin + 1
            count_amount[amount] = -1 if min_coins_amt == float('inf') else min_coins_amt
            return count_amount[amount]
        if amount <= 0:
            return 0
        count_amount = defaultdict(lambda: float('inf'))
        coin_change_for_amount(coins, amount)
        return count_amount[amount]
