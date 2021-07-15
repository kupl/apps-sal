class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count = collections.defaultdict(int)
        def coinChangeHelper(coins, rem, count):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if count[rem] != 0:
                return count[rem]
            minCount = 2**32
            for coin in coins:
                makeChange = coinChangeHelper(coins, rem - coin, count)
                if makeChange > -1 and makeChange < minCount:
                    minCount = makeChange + 1
            
            count[rem] = -1 if minCount == 2 ** 32 else minCount
            return count[rem]
        
        return coinChangeHelper(coins, amount, count)
