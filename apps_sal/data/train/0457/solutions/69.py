class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        values = [-1 for i in range(amount + 1)]
        values[0] = 0
        for i in coins:
            for j in range(1, len(values)):
                if j >= i:
                    if values[j - i] == -1:
                        continue
                    curr_num_coins = 1 + values[j - i]
                    if values[j] == -1 or values[j] > curr_num_coins:
                        values[j] = curr_num_coins
        return values[amount]
