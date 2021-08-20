class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        rows = amount + 1
        cols = len(coins) + 1
        cache = [[0 for _ in range(cols)] for _ in range(rows)]
        for row in range(1, rows):
            cache[row][0] = -1
        for row in range(1, rows):
            for col in range(1, cols):
                newAmt = row - coins[col - 1]
                takeValue = cache[newAmt][col] if newAmt >= 0 and newAmt < len(cache) else -1
                takeCoin = 1 + takeValue if takeValue >= 0 else -1
                skipCoin = cache[row][col - 1]
                if skipCoin < 0:
                    cache[row][col] = takeCoin
                elif takeCoin < 0:
                    cache[row][col] = skipCoin
                else:
                    cache[row][col] = min(skipCoin, takeCoin)
        return cache[amount][len(coins)]
