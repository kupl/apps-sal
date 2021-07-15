class Solution:
    def minDifficulty(self, arr: List[int], d: int) -> int:
        if len(arr)<d:
            return -1
        memo = [[None]*(d+1) for _ in range(len(arr)+1)]
        def dp(jobs, days):
            if days <0:
                return -1
            if memo[jobs][days] is not None:
                return memo[jobs][days]
            if jobs < days:
                memo[jobs][days] = -1
                return -1
            if d == 1:
                memo[jobs][days] = max(arr[:jobs])
                return max(arr[:jobs])
            if jobs==days:
                memo[jobs][days] = sum(arr[:jobs])
                return sum(arr[:jobs])
            res = -1
            rm = arr[jobs-1]
            for i in range(1, jobs+1):
                rm = max(rm, arr[jobs-i])
                temp = dp(jobs-i, days-1)
                if temp!=-1:
                    if res == -1:
                        res = temp + rm
                    else:
                        res = min(res, temp+rm)
            memo[jobs][days] = res
            return res
        return dp(len(arr), d)
    
#     import functools
    
#     def minDifficulty1(self, A, d):
#         calls = 0
#         n = len(A)
#         if n < d: return -1

#         @functools.lru_cache(None)
#         def dfs(i, d):
#             nonlocal calls
#             calls += 1
#             if d == 1:
#                 return max(A[i:])
#             res, maxd = float('inf'), 0
#             for j in range(i, n - d + 1):
#                 maxd = max(maxd, A[j])
#                 res = min(res, maxd + dfs(j + 1, d - 1))
#             return res
#         res = dfs(0, d)
#         print(calls)
#         return res

