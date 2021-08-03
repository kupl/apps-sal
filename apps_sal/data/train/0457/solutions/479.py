class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}

        def helper(amt):
            if amt < 0:
                return -1
            elif amt == 0:
                return 0
            elif amt in mem:
                return mem[amt]
            min_coins = float('inf')
            for coin in coins:
                result = helper(amt - coin)
                if result != -1:
                    min_coins = min(min_coins, 1 + result)
            mem[amt] = min_coins
            return min_coins
        output = helper(amount)
        return -1 if output == float('inf') else output
