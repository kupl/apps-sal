class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        return self.aux(coins, amount, memo)

    def aux(self, coins, amount, memo):
        if amount < 0:
            return -1

        if amount == 0:
            return 0

        if amount in memo.keys():
            return memo[amount]

        minimum = 999999999

        for x in coins:
            temp = self.aux(coins, amount - x, memo)
            if temp < minimum and temp >= 0:
                minimum = temp

        if minimum == 999999999:
            memo[amount] = -1
            return memo[amount]

        memo[amount] = 1 + minimum

        return memo[amount]
