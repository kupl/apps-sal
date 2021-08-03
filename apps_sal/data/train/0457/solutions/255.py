
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        memo = {x: amount + 1 for x in range(amount + 1)}
        memo[0] = 0

        for i in range(amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    memo[i] = min(memo[i], 1 + memo[i - coins[j]])

        if memo[amount] < amount + 1:
            return memo[amount]
        else:
            return -1
