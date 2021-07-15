class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        use dp 0 - 11
        '''
        if amount == 0:
            return 0
        
        dp = [None] * amount
        dp[0] = 1 if 1 in coins else -1
        
        for i in range(1, amount):
            min_req = float('inf')
            
            for c in coins:
                if (i + 1) % c == 0:
                    min_req = min(min_req, (i + 1) // c)
                elif (i + 1) // c > 0 and dp[i - c] != -1:
                    min_req = min(min_req, dp[i - c] + 1)
            
            if min_req == float('inf'):
                dp[i] = -1
            else:
                dp[i] = min_req
        
        return dp[-1]
