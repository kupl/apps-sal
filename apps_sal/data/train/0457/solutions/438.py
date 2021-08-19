class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        t = [[0 for x in range(amount + 1)] for x in range(len(coins) + 1)]
        for j in range(amount + 1):
            t[0][j] = 1000
        for i in range(1, len(coins) + 1):
            t[i][0] = 0
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j % coins[i - 1] == 0:
                    t[i][j] = j / coins[i - 1]
                else:
                    t[i][j] = 1000
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] <= j:
                    t[i][j] = min(t[i][j - coins[i - 1]] + 1, t[i - 1][j])
                else:
                    t[i][j] = t[i - 1][j]
        if t[len(coins)][amount] != 1000:
            return t[len(coins)][amount]
        return -1
