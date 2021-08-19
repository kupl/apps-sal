class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        values = [-1 for i in range(amount + 1)]
        values[0] = 0

        # loop through all coins
        for i in coins:
            # loop through values for coins to add up to
            for j in range(1, len(values)):
                # check if current coin is greater than value
                if j >= i:
                    # continue if no possible combinations
                    if values[j - i] == -1:
                        continue
                    curr_num_coins = 1 + values[j - i]
                    # check if number of coins for value is already fewer
                    if values[j] == -1 or values[j] > curr_num_coins:
                        # update current minimum coins required
                        values[j] = curr_num_coins
        return values[amount]
