class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        w = amount

        t = [[0 for i in range(w + 1)] for j in range(n + 1)]

        for i in range(n + 1):
            for j in range(w + 1):
                if i == 0:
                    t[i][j] = float('inf')
                if j == 0:
                    t[i][j] = 0
                if i == 1 and j > 0:
                    if j % coins[0] == 0:
                        t[i][j] = j // coins[0]
                    else:
                        t[i][j] = float('inf')

        for i in range(2, n + 1):
            for j in range(1, w + 1):
                if coins[i - 1] <= j:
                    t[i][j] = min(t[i - 1][j], 1 + t[i][j - coins[i - 1]])
                else:
                    t[i][j] = t[i - 1][j]
        if t[n][w] == float('inf'):
            return -1
        return t[n][w]
