class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        In this case we define teh recursive relationship as follows:
        Where Opt(S) is the minimum number of coins in [c1, c2, .., cn] that are needed to create amount S. 

        The following recursive relationship holds:
        Opt(S) = Opt(S - C) + 1, where C is the denomination of [c0, c1, ..., cn-1] and S is the amount.   

        Minimum number of coins for amoun S in denomination cn, is given by the minimum amount of (amount - previouse denomination) for all coins.  

        But we dont know the denomination of the last coin C, so we compute 
        Opt(S - ci) for all possible denominations c0, c1, ..., cn, and choose the minimum among them. 

        Subject to S - ci >= 0. 

        Base cases:
        Opt(S) = 0, when S = 0. S is the amount.
        Opt(S) = -1, when n = 0. 

        * Each sub porblem (coin) has S computations. 
        * And the number of subproblems is O(n * S). 

        '''

        T = [float('inf')] * (amount + 1)
        T[0] = 0

        for amnt in range(1, amount + 1):
            curr_min = float('inf')
            for k in range(len(coins)):
                if coins[k] <= amnt:
                    val = 1 + T[amnt - coins[k]]
                    if val < curr_min:
                        curr_min = val

            T[amnt] = curr_min

        return -1 if T[-1] == float('inf') else T[-1]
