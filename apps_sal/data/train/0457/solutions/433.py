class Solution:

    def coinChange(self, coins, amount):
        if amount < 1:
            return 0

        def count_change(coins, amount, dic={}):
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            if amount in dic:
                return dic[amount]
            minimum = float('inf')
            for i in range(len(coins)):
                current = count_change(coins, amount - coins[i], dic)
                if current >= 0 and current < minimum:
                    minimum = 1 + current
            if minimum == float('inf'):
                dic[amount] = -1
            else:
                dic[amount] = minimum
            return dic[amount]
        return count_change(coins, amount, {})
