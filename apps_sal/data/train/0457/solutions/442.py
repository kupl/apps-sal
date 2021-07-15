class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #d(m,n) indicates using upto the first m kinds of coins, the number of fewest coins needed to make up to n
        coins.sort()
        n = len(coins)
        
        d = [[-1] * (amount + 1) for i in range(n + 1)]
        
        for i in range(amount + 1):
            if i % coins[0] == 0:
                d[1][i] = i // coins[0]
        for i in range(n + 1):
            d[i][0] = 0
        for i in range(2, n + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] >= 0:
                    if d[i - 1][j] != -1 and d[i][j - coins[i - 1]] != -1:
                        d[i][j] = min(d[i - 1][j], d[i][j - coins[i - 1]] + 1)
                    elif d[i - 1][j] == -1 and d[i][j - coins[i - 1]] != -1:
                        d[i][j] = d[i][j - coins[i - 1]] + 1
                    elif d[i - 1][j] != -1 and d[i][j - coins[i - 1]] == -1:
                        d[i][j] = d[i - 1][j]
                    else:
                        d[i][j] = d[i - 1][j]
                else:
                    d[i][j] = d[i - 1][j]

        return d[n][amount]
        

