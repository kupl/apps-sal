class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # In any dp probelm we need to identify the recursive relationship.
        # The solution to a problem can be found with teh help of its sub problems.
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
        # What will we identify subproblems by. (S - ci)
        # or by an amount. So as we are calculating the minimum number of coind needed for each amount, we need to look at the minimum number of coins need using c0, c1, .., cn.
        # Sub problems are determined by amounts, so we cache them by amount.
        # Fir every sub problem need optimal number of coins for each denomination. Then we take the minimum of all teh minimums, and that is the minimum number of coins needed to represnet an amount.

        T = [float('inf')] * (amount + 1)
        T[0] = 0

        # In an iteratoive solution we move left to right and have to compute teh minimum number of coins for all amounts before this one.

        for amnt in range(1, amount + 1):
            curr_min = float('inf')
            for k in range(len(coins)):
                # calculate the minimum number of coins needed for each denotion to represnet the amount given by amnt.
                # then take minimum and assign it to T[amnt].
                if coins[k] <= amnt:
                    val = 1 + T[amnt - coins[k]]
                    if val < curr_min:
                        curr_min = val

            T[amnt] = curr_min

        return -1 if T[-1] == float('inf') else T[-1]
