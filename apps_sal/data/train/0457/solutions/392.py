class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [[float('inf') for _ in range(amount + 1)] for _ in range(len(coins))]
        for x in range(len(coins)):
            memo[x][0] = 0
        for (i, coin) in enumerate(coins):
            for tot in range(1, amount + 1):
                if i > 0:
                    memo[i][tot] = memo[i - 1][tot]
                if coin <= tot:
                    memo[i][tot] = min(memo[i][tot], memo[i][tot - coin] + 1)
        out = memo[len(coins) - 1][amount]
        return -1 if out == float('inf') else out
