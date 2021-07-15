class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        n = len(stoneValue)
        dp = [float('-inf')] * n
        dp[-1] = stoneValue[-1]
        for i in range(n - 2, -1, -1):
            s = 0
            for j in range(i, i + 3):
                s += stoneValue[j] if j < n else 0
                nxt = dp[j + 1] if j + 1 < n else 0
                dp[i] = max(dp[i], s - nxt)
        
                
                
#         @lru_cache(None)
#         def dp(cur):
#             if cur == len(stoneValue) - 1:
#                 return stoneValue[cur]
#             if cur >= len(stoneValue):
#                 return 0
#             ret = float('-inf')
#             s = 0
#             for i in range(3):
#                 nxt = dp(cur + i + 1)
#                 s += stoneValue[cur + i] if cur + i < len(stoneValue) else 0
#                 ret = max(ret, s - nxt)
#             return ret

#         ans = dp(0)
        ans = dp[0]
        if ans > 0:
            return 'Alice'
        elif ans < 0:
            return 'Bob'
        else:
            return 'Tie'

            

