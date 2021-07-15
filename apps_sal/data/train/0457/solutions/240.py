class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def my_coinChange(coins, rem, count):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if count[rem - 1] != 0:
                return count[rem - 1]

            my_min = float('inf')

            for coin in coins:
                res = my_coinChange(coins, rem - coin, count)
                if res >= 0 and res < my_min:
                    my_min = 1 + res

            count[rem - 1] = -1 if my_min == float('inf') else my_min
            return count[rem - 1]
        
        if amount < 1:
            return 0
        return my_coinChange(coins, amount, [0] * amount)
    

