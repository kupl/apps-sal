class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # use DP
        N = len(coins)
        M = amount
        table = [-1] * (M + 1)
        for j in range(N + 1):
            table[0] = 0
        for m in range(1, M + 1):
            for i in range(N):
                c = coins[i]
                if c > m:
                    pass
                elif table[m - c] != -1:
                    if table[m] != -1:
                        table[m] = min(table[m - c] + 1, table[m])
                    else:
                        table[m] = table[m - c] + 1
        return table[M]
