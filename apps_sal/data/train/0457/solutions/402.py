class Solution:

    def coinChange(self, coin: List[int], sum1: int) -> int:
        maxv = float('inf') - 1
        n = len(coin)
        t = [[0 for j in range(sum1 + 1)] for i in range(n + 1)]
        for i in range(n + 1):
            for j in range(sum1 + 1):
                if i == 0 and j == 0:
                    t[i][j] = maxv
                elif j == 0:
                    t[i][j] = 0
                elif i == 0:
                    t[i][j] = maxv
        for i in range(1, n + 1):
            for j in range(1, sum1 + 1):
                if coin[i - 1] <= j:
                    t[i][j] = min(t[i][j - coin[i - 1]] + 1, t[i - 1][j])
                else:
                    t[i][j] = t[i - 1][j]
        if t[n][sum1] == float('inf'):
            return -1
        return t[n][sum1]
