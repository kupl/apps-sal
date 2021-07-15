class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
#         cumsum = [0]*(n+1)
#         for i in range(1,n+1):
#             cumsum[i] = cumsum[i-1] + stoneValue[i-1]
        
#         @functools.lru_cache(None)
#         def helper(i, turn):
#             if turn == 0:
#                 if i == n:
#                     return 0
#                 if i == n-1:
#                     return stoneValue[-1]
#                 return max([cumsum[i+k]-cumsum[i] + helper(i+k,1) for k in [1,2,3] if i+k <= n])
#             else:
#                 if i == n:
#                     return 0
#                 if i == n-1:
#                     return 0
#                 return min([helper(i+k,0) for k in [1,2,3] if i+k <= n])
            
#         c = helper(0,0)
#         if c > sum(stoneValue) / 2.0:
#             return 'Alice'
#         elif c == sum(stoneValue) / 2.0:
#             return 'Tie'
#         else:
#             return 'Bob'
        A = stoneValue
        dp = [0] * 3
        for i in range(n - 1, -1, -1):
            dp[i % 3] = max(sum(A[i:i + k]) - dp[(i + k) % 3] for k in (1, 2, 3))
        c = dp[0]
        if c > 0:
            return 'Alice'
        elif c == 0:
            return 'Tie'
        else:
            return 'Bob'
