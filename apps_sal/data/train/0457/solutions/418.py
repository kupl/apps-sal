class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[0 for j in range(amount + 1)] for i in range(len(coins) + 1)]

        for i in range(len(coins) + 1):
            dp[i][0] = 0
        for j in range(1, amount + 1):
            dp[0][j] = float('inf') - 1

        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] <= j:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[len(coins)][amount] if dp[len(coins)][amount] != float('inf') else -1
        '''
        def coin_change_2(coins,n,amount):
            if n==0:
                return float('inf')-1
            if amount==0:
                return 0
            if coins[n-1]<=amount:
                return min(coin_change_2(coins,n-1,amount),1+coin_change_2(coins,n,amount-coins[n-1]))
            else:
                return coin_change_2(coins,n-1,amount)
        
        n=len(coins)
        ans = coin_change_2(coins,n,amount)
        return ans if ans  != float('inf') else -1
        '''
