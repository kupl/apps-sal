class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[0]*(amount+1)
        for i in range(1, amount+1):
            minn=float('inf')
            for j in coins:
                if i==j:
                    minn=min(minn, 1)
                    continue
                if i-j>0:
                    minn=min(minn, 1+dp[i-j])
            dp[i]=minn
        return dp[amount] if dp[amount]!=float('inf') else -1
#         if amount==0:
#             return 0
#         if amount<0:
#             return -1
#         minn=float('inf')
#         for i in coins:
#             count=self.coinChange(coins, amount-i)
#             if count!=-1:
#                 minn=min(count+1, minn)

#         return minn if minn!=float('inf') else -1

