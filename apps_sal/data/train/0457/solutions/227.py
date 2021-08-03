class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        11 -> 0

        10 -> 1 -> (6 -> 5)
        9 -> 1
        6 -> 1


        '''

        def helper(remAmt, coins):
            nonlocal mem

            if remAmt in mem:
                return mem[remAmt]

            minCoins = float('inf')

            for coin in coins:
                if coin <= remAmt:
                    result = 1 + helper(remAmt - coin, coins)
                    minCoins = min(minCoins, result)
                else:
                    break

            mem[remAmt] = minCoins
            return minCoins

        if amount < 1:
            return 0

        mem = {0: 0}
        coins.sort()
        minCoins = helper(amount, coins)
        if minCoins == float('inf'):
            return -1
        return minCoins
