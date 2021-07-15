class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
#         self.rollMax = tuple(rollMax)
        
#         @lru_cache(None)
#         def helper(n, ban):
#             times = 0
#             if n == 1:
#                 for t in ban:
#                     if t > 0:
#                         times += 1
#                 return times

#             for i, t in enumerate(ban):
#                 if t > 0:
#                     cur = tuple()
#                     for j in range(len(ban)):
#                         if i == j:
#                             cur += (ban[j]-1,)
#                         else:
#                             cur += (self.rollMax[j], )
#                     times += helper(n-1, cur)

#             return times % (10**9 + 7)
        
#         return helper(n, tuple(rollMax))
        dp = [[0] * (len(rollMax) + 1) for _ in range(n + 1)]
        for j in range(len(rollMax)):
            dp[1][j] = 1
            dp[1][-1] += dp[1][j]
        
        for i in range(2, n + 1):
            for j in range(len(rollMax)):
                dp[i][j] = dp[i - 1][-1]
                k = i - rollMax[j]
                if k == 1:
                    dp[i][j] -= 1
                elif k > 1:
                    dp[i][j] -= (dp[k - 1][-1] - dp[k - 1][j])
                dp[i][-1] += dp[i][j]
        return dp[n][len(rollMax)] % int(1e9 + 7)
