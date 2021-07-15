class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[0]*(amount+1)
        for i in range(1,len(dp)):
            dp[i]=float('inf')
            for j in coins:
                if i>=j and dp[i-j]+1<dp[i]:
                    dp[i]=dp[i-j]+1
        return -1 if dp[amount]==float('inf') else dp[amount]

