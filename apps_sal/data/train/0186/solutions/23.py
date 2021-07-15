from functools import lru_cache

class Solution:
    # def largestNumber(self, cost: List[int], target: int) -> str:
#         def compare(a, b):
#             if len(a) == 0:
#                 return b
#             if sum(a) > sum(b):
#                 return a
#             elif sum(b) > sum(a):
#                 return b
#             else:
#                 j = -1
#                 while j >= -len(a) and a[j] == b[j]:
#                     j -= 1
#                 if j < -len(a):
#                     return a
#                 if a[j] >= b[j]:
#                     return a
#                 else:
#                     return b
                
#         @lru_cache(None)
#         def dfs(idx, tgt):
#             if idx == 0:
#                 if tgt != 0:
#                     return []
#             if tgt == 0:
#                 return [0, 0, 0, 0, 0, 0, 0, 0, 0]
#             out = []
#             for i in range(tgt // cost[idx] + 1):
#                 nxt = dfs(idx - 1, tgt - i * cost[idx])
#                 # print(nxt, i)
#                 if len(nxt) != 0:
#                     new = [x for x in nxt]
#                     new[idx] += i
#                     out = compare(out, new)
#             return out
        
#         ans = '' 
#         r = dfs(8, target)
#         for i, x in enumerate(r):
#             ans += str(i + 1) * x
#         return ans

        def largestNumber(self, cost, target):
            dp = [0] + [-1] * (target + 5000)
            for t in range(1, target + 1):
                dp[t] = max(dp[t - c] * 10 + i + 1 for i, c in enumerate(cost))
            return str(max(dp[t], 0))
