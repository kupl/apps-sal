class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        dp = {0: 0}
        for r in rods:
            dp2 = dp.copy()
            for d in list(dp.keys()):
                dp2[d + r] = max(dp2.get(d + r, 0), dp[d])
                dp2[abs(d - r)] = max(dp2.get(abs(d - r), 0), dp[d] + min(d, r))
            dp = dp2
        # print(dp)
        return dp[0]
    
    
        # dp = {0: 0}
        # for x in rods:
        #     for d, y in dp.items():
        #         dp[d + x] = max(dp.get(x + d, 0), y)
        #         dp[abs(d - x)] = max(dp.get(abs(d - x), 0), y + min(d, x))
        # return dp[0]
        
        
        
#         @lru_cache(None)
#         def dp(i, s):
#             if i == len(rods):
#                 return 0 if s == 0 else float(\"-inf\")
#             return max(dp(i + 1, s), dp(i + 1, s - rods[i]), dp(i + 1, s + rods[i]) + rods[i])
        
#         return dp(0, 0)
        
        
        
        
#         dp = {}
#         dp[0] = 0
        
#         for i in rods:
#             cur = collections.defaultdict(int)
#             for s in dp:
#                 cur[s+i] = max(dp[s] + i, cur[s+i])
#                 cur[s] = max(dp[s], cur[s])
#                 cur[s-i] = max(dp[s], cur[s-i])
#             dp = cur
#         return dp[0]

