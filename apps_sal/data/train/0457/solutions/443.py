class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        n_coins = len(coins)
        least_coin = coins[0]
        max_amount = amount + 1
        mat = [[0 for i in range(amount + 1)] for i in range(n_coins + 1)]
        if amount == 0:
            return 0
        if amount < least_coin:
            return -1
        for i in range(amount + 1):
            if i % least_coin == 0:
                mat[1][i] = i // least_coin
            else:
                mat[1][i] = -1
        for i in range(2, n_coins + 1):
            for j in range(1, amount + 1):
                curr_coin = coins[i - 1]
                if j - curr_coin >= 0:
                    if mat[i][j - curr_coin] == -1:
                        mat[i][j] = mat[i - 1][j]
                    elif mat[i - 1][j] == -1:
                        mat[i][j] = 1 + mat[i][j - curr_coin]
                    elif mat[i][j - curr_coin] == -1 and mat[i - 1][j] == -1:
                        mat[i][j] = -1
                    else:
                        mat[i][j] = min(1 + mat[i][j - curr_coin], mat[i - 1][j])
                else:
                    mat[i][j] = mat[i - 1][j]
        return mat[-1][-1]
