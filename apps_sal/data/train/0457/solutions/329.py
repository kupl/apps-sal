class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        M = amount
        table = [[-1] * (N + 1) for i in range(M + 1)]
        for j in range(N + 1):
            table[0][j] = 0
        for m in range(1, M + 1):
            for i in range(N):
                c = coins[i]
                if c > m:
                    table[m][i + 1] = table[m][i]
                elif table[m - c][i + 1] != -1:
                    if table[m][i] != -1:
                        table[m][i + 1] = min(table[m - c][i + 1] + 1, table[m][i])
                    else:
                        table[m][i + 1] = table[m - c][i + 1] + 1
                else:
                    table[m][i + 1] = table[m][i]
        return table[M][N]
