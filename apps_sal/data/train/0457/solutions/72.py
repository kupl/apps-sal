class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = amount + 1
        coins.sort(reverse=True)
        dp = [MAX] * (MAX)
        dp[0] = 0
        for i in range(1, MAX):
            dp[i] = min([dp[i - c] if i >= c else (MAX) for c in coins])  # List Comprehension is faster
            dp[i] = dp[i] + 1 if dp[i] != MAX else dp[i]
        return -1 if (dp[-1] == MAX) else dp[-1]

#         coins.sort()
#         return self.countCoins(coins,amount,len(coins),0)

#     def countCoins(self,coins,amount,idx,count):
#         if idx < 0:
#             return -1
#         elif amount - 1 or count < 0:
#             return float('inf')
#         c = amount//coins[idx]
#         rem = amount % coins[idx]
#         if rem == 0:
#             return count+c
#         else:
#             return self.countCoins(coins,rem,idx-1,count+c)
