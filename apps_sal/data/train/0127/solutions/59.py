# from functools import lru_cache
# class Solution:
#     def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
#         MOD = 10**9+7
#         n = len(profit)
#         psum = profit + [0]
#         for i in range(n)[::-1]:
#             psum[i] += psum[i+1]
#         # print(psum)
#         @lru_cache(None)
#         def dfs(g, p, idx):
#             if g < 0 or p > psum[idx]:
#                 return 0
#             if idx == n:
#                 return 1
#             res = (dfs(g, p, idx+1) + dfs(g-group[idx], p-profit[idx], idx+1))%MOD
#             # print(g,p,idx,res)
#             return res
#         return dfs(G,P,0)


from functools import lru_cache


class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(profit)
        psum = profit + [0]
        for i in range(n)[::-1]:
            psum[i] += psum[i + 1]
        # print(psum)

        @lru_cache(None)
        def dfs(g, p, idx):
            # if g < 0 or p > psum[idx]:
            #     return 0
            # if idx == n:
            #     return 1
            if g < 0:
                return 0
            if idx == n:
                return 1 if p <= 0 else 0
            p = max(p, 0)
            res = (dfs(g, p, idx + 1) + dfs(g - group[idx], p - profit[idx], idx + 1)) % MOD
            # print(g,p,idx,res)
            return res
        return dfs(G, P, 0)
