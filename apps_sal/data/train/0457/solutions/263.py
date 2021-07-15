class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [[float('inf')]*(amount + 1) for _ in range(len(coins) + 1)]
        # for any amount, no coins
        for i in range(len(coins) + 1):
            cache[i][0] = 0
            
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    cache[i][j] = min(cache[i - 1][j], cache[i][j - coins[i - 1]] + 1)
                else:
                    cache[i][j] = cache[i - 1][j]

        return cache[-1][-1] if cache[-1][-1] != float('inf') else -1


    # Recurrence Relation
    # base case: no coins, any amount > 0: -1
    #            any number of coins (even 0), amount 0: 0 coins
    #
    # For any new coin i, either use the coin or don't use it to reach the amount j
    # If not using coin: num_coins[i][j] = num_coins[i - 1][j] same as num coins without that coin
    # If using coin: num_coins[i][j] = num_coins[i][j - coins[i]] + 1 num coins with (or without) that coin and an amount (amount - coin_value) plus 1
    # Take minimum between using/not using coin
    
    # Can build this up from no coins at all
    #      amount
    # coins , , , ,

