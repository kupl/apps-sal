class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        similar to knapsack problem, except we want minimum coins instead of max items


        dp: increase coins and amount one at a time

           ''   1.   2.   5
        0  0.   0.   0.   0
        1  -1   1    1    1
        2  -1   2    1    1 
        3  -1   3.   2.   2
        4  -1   4.   2.   2
        5  -1   5.   3.   1
        6  -1   6.   3.   2
        7  -1   7.   4.   2
        8  -1   8.   4.   3
        9  -1   9.   5.   3
        10 -1   10.  5.   2
        11 -1   11.  6.   3

        fewest_coins[amount][coins_i + 1] = min of (1 + fewest_coins[amount-coins[j]][coins_i]) for j in range(coins_i+1) or -1 if all the fewest_coins[amount-coins[j]][coins_i] are -1

        how to effectively start dp array?

        '''

        # fewest_coins = [[0 for i in range(len(coins)+1)] for j in range(amount+1)]
        fewest_coins = [0 for j in range(amount + 1)]

#         for i in range(len(coins)+1):
#             fewest_coins[0][i] = 0

#         for j in range(1,amount+1):
#             fewest_coins[j][0] = -1

        # for j in range(1,amount+1):
        #     fewest_coins[j][0] = -1

        for j in range(1, amount + 1):
            fewest_coins[j] = float('inf')
            for coin_i in range(len(coins)):
                if coins[coin_i] == j:
                    fewest_coins[j] = 1
                    break
                elif coins[coin_i] < j:
                    if fewest_coins[j - coins[coin_i]] > 0:
                        fewest_coins[j] = min(fewest_coins[j], fewest_coins[j - coins[coin_i]] + 1)
            if fewest_coins[j] == float('inf'):
                fewest_coins[j] = -1
#         for j in range(1,amount+1):
#             for i in range(1,len(coins)+1):

#                 fewest_coins[j][i] = float('inf')
#                 for coin_i in range(i):
#                     if coins[coin_i] == j:
#                         fewest_coins[j][i] = 1
#                         break
#                     elif coins[coin_i] < j:
#                         if fewest_coins[j-coins[coin_i]][i] > 0:
#                             fewest_coins[j][i] = min(fewest_coins[j][i], fewest_coins[j-coins[coin_i]][i]+1)
#                 if fewest_coins[j][i] == float('inf'):
#                     fewest_coins[j][i] = -1

        return fewest_coins[-1]
