class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        self.cache=[0] * (amount + 1)
        return self.coin_change(coins, amount)

    def coin_change(self, coins, remainder):
        if remainder < 0:
            return -1

        if remainder == 0:
            return 0

        if self.cache[remainder] != 0:
            return self.cache[remainder]

        system_max = sys.maxsize
        minimum = system_max
        for coin in coins:
            change_result = self.coin_change(coins, remainder - coin)

            if (change_result >= 0 and change_result < minimum):
                minimum = 1 + change_result

        self.cache[remainder] = -1 if (minimum == system_max) else minimum

        return self.cache[remainder]
#         if not coins:
#             return 0
#         dp = [float(\"inf\") for _ in range(amount + 1)]
        
#         dp[0]=0
#         for i in range(1,amount+1):
#             for coin in coins:
#                 if i>=coin:
#                     dp[i] = min(dp[i],dp[i-coin]+1)
#         if dp[amount]!= float(\"inf\"):
#             return dp[-1]
#         else:
#             return -1
            
#         \"\"\"
#         #1  Return 0 if there are no given coins
#         \"\"\"
#         if not coins:
#             return 0
        
#         \"\"\"
#         #2  Initialize a 'dp' array of a size of the given amount (inclusive, hence +1).
#         #   Initialize each index element to be an arbitary number. In this case I chose amount + 1. E.g.: 11 + 1 = 12
#         \"\"\"
#         dp = [float(\"inf\") for _ in range(amount + 1)]
        
#         \"\"\"
#         #3  Base case. Make the first cell 0 because if amount is 0, you do not need any coin to make up to that amount
#         #   stdout: dp = [0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
#         \"\"\"
#         dp[0] = 0
        
#         \"\"\"
#         #4  Look through the entire 'dp' array, for each of the index element, we will check it against the list(array) of given coins.
#         #   'i' in this case is the amount we want to compute from bottom-up starting from 0 to the 'amount' that the question asks for
#         #   E.g.: [0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12] vs [1, 2, 5]
#                    ^                   ^                           ^             
#                    amount 0            amount 5                    amount = 11 (this is what we want)             
#         \"\"\"
#         for i in range(1, amount+1):
#             for coin in coins:
#                 \"\"\"
#                 #5  If 'i' (the current amount we want to find, is less than 'coin', we will skip that. Otherwise compute it:
#                 #   Because it does not make sense to compute the coin if the coin itself is already larger than the amount that we're looking at
#                 \"\"\"
#                 if i >= coin:
#                     \"\"\"
#                     #6  We shall update each dp[i] to be the minimum between itself vs it's previous computed answer dp[i-coin]. 
#                     #   And we do this for each available coin. Only if 'coin' is smaller than the amount 'i'
#                     #   We do '+1' for dp[i-coin] + 1 here because it costs us a step to do so
#                     \"\"\"
#                     dp[i] = min(dp[i], dp[i-coin] + 1)
        
#         \"\"\"
#         #7  By the end of the 2 for loops, you will end up with 
#         #   stdout: [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
        
#         #8  So if the dp[amount] is not the original amount we initialized at Step #3. Then we shall return the dp[amount] that was asked by the question
#         \"\"\"
#         if dp[amount] != float(\"inf\"):
#             return dp[amount]
#         else:
#             return -1
        
#         \"\"\"
#         #9  Else. If the dp[amount] is still amount + 1 as we initialized. It means there were no suitable coins for this scenario and -1 is returned
#         \"\"\"
    
#         # key:amount value:min number of coins for the amount
    

