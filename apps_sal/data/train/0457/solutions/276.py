class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins_sorted = list(sorted(coins, reverse=True))
        memo = {}

        def choose(amount):
            if amount in memo:
                return memo[amount]
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            memo[amount] = -1
            for c in coins_sorted:
                if (ret := choose(amount - c)) >= 0:
                    if memo[amount] != -1:
                        memo[amount] = min(memo[amount], ret + 1)
                    else:
                        memo[amount] = ret + 1
            return memo[amount]

        return choose(amount)
