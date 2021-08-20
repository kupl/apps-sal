class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [[float('inf')] * (amount + 1) for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            cache[i][0] = 0
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    cache[i][j] = min(cache[i - 1][j], cache[i][j - coins[i - 1]] + 1)
                else:
                    cache[i][j] = cache[i - 1][j]
        return cache[-1][-1] if cache[-1][-1] != float('inf') else -1
