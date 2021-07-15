import functools as ft
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        const = 10**9+7
        cache = {}
        matr = [[False]*10 for i in range(40)]
        maxx = -1
        for j in range(len(hats)):
            for i in hats[j]:
                matr[i-1][j] = True
                maxx = max(i-1, maxx)
        def s(mask_p, h, n):
            if n == 0:
                return 1
            if h < 0 or n > h+1:
                return 0
            c = str(mask_p + [h])
            if c in cache:
                return cache[c]
            res = s(mask_p, h-1, n)
            for p in range(len(matr[h])):
                if mask_p[p] and matr[h][p]:
                    mask_p[p] = False
                    res += s(mask_p, h-1, n-1)
                    mask_p[p] = True
            cache[c] = res
            return res
        mask_p = [True]*len(hats) + [False]*(10-len(hats))
        return s(mask_p, maxx, len(hats))%const
