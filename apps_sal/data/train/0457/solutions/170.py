import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        [1,2,3] 7 => 3
        
        7-3 = 4
        4-3 = 1
        1-3 = -2 not possible
        1-2 = -1 not
        1-1 = 0 return 
        0 1 2 3 4 5 6 7
        3 2 2 2 1 1 1 1
              &
        '''
        dp = [sys.maxsize] * (amount+1)
        if amount==0: return 0
        dp[amount] = 0
        for i in range(amount,-1,-1):
            for coin in coins:
                if i-coin >= 0:
                    dp[i-coin] = min(dp[i]+1, dp[i-coin])
        return -1 if dp[0] == sys.maxsize else dp[0]
