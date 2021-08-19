from functools import lru_cache
import numpy as np


class Solution:
    def __init__(self):
        self.cache = {}
        self.res = np.inf

    def tilingRectangle(self, n: int, m: int) -> int:
        def tilingRectangleCalc(state, cnt):
            if cnt > self.res:
                return
            state = list(state)
            minHeight = min(state)
            if minHeight == n:
                self.res = min(self.res, cnt)
                return
            minIdx = state.index(minHeight)
            maxL = 1
            while minIdx + maxL - 1 <= m - 1 and state[minIdx + maxL - 1] == minHeight:
                maxL += 1
            for l in range(maxL - 1, 0, -1):
                if minHeight + l > n:
                    continue
                s = tuple(state[:minIdx] + [minHeight + l] * l + state[minIdx + l:])
                if s in self.cache and self.cache[s] < cnt + 1:
                    continue
                self.cache[s] = cnt + 1
                tilingRectangleCalc(s, cnt + 1)
            return
        if m > n:
            n, m = m, n
        tilingRectangleCalc(tuple([0] * m), 0)
        return self.res


# class Solution:
#     def tilingRectangle(self, n: int, m: int) -> int:
#         @lru_cache(None)
#         def tilingRectangleCalc(state):
#             state=list(state)
#             minHeight=min(state)
#             if minHeight==n:
#                 return 0
#             minIdx=state.index(minHeight)
#             res=np.inf
#             for l in range(1,n-minHeight+1):
#                 if minIdx+l-1>m-1 or state[minIdx+l-1]>minHeight:
#                     break
#                 res=min(res,tilingRectangleCalc(tuple(state[:minIdx]+\\
#                                                       [minHeight+l]*l+state[minIdx+l:])))
#             return 1+res
#         if m>n:
#             n,m=m,n
#         return tilingRectangleCalc(tuple([0]*m))
