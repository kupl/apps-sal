class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        t = [[-1] * (amount + 1)] * (len(coins) + 1)

        for i in range(len(t)):
            for j in range(len(t[0])):
                if j == 0:
                    t[i][j] = 0
                if i == 0:
                    t[i][j] = float('inf') - 1
        for j in range(1, amount + 1):
            if j % coins[0] == 0:
                t[1][j] = int(j / coins[0])
            else:
                t[1][j] = float('inf') - 1
        for i in range(2, len(t)):
            for j in range(2, len(t[0])):
                if coins[i - 1] <= j:
                    t[i][j] = min(1 + t[i][j - coins[i - 1]], t[i - 1][j])
                else:
                    t[i][j] = t[i - 1][j]
        if t[-1][-1] != float('inf'):
            return t[-1][-1]
        return -1
