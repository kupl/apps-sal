class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()
        table = [[-1 for i in range(amount + 1)] for i in range(len(coins))]

        for i in range(len(coins)):
            for j in range(amount + 1):
                if coins[i] > j and i > 0 and table[i-1][j] > 0:
                    table[i][j] = table[i-1][j]
                elif j >= coins[i]:
                    x = j - coins[i]
                    pre_val = 9999999
                    calculated_val = 0
                    if i > 0 and table[i - 1][j] > 0:
                        pre_val = table[i - 1][j]
                        
                    if x > 0:
                        if table[i][x] > 0:
                            calculated_val = table[i][x]
                            table[i][j] = min(1 + calculated_val, pre_val)
                        else:
                            if i > 0 and pre_val != 9999999:
                                table[i][j] = pre_val
                    elif x == 0:
                        table[i][j] = min(1 + calculated_val, pre_val)
        return table[len(coins)-1][amount]
                
                

