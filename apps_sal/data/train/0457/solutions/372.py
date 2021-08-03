class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):

            for coin in coins[::-1]:
                j = i - coin
#                print('i,j,coin=',i,j,coin)
                if j < 0 or dp[j] == -1:
                    continue
                if dp[i] == -1:
                    dp[i] = dp[j] + 1
                else:
                    dp[i] = min(dp[i], dp[j] + 1)

        return(dp[amount])
