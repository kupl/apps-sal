import functools as ft


class Solution:
    # def numberWays(self, hats: List[List[int]]) -> int:
    #     cache = {}
    #     l = len(hats)
    #     def f(allowed, i):
    #         if i == l:
    #             return 1
    #         key = (tuple(allowed), i)
    #         if key in cache:
    #             return cache[key]
    #         c = 0
    #         for hat in hats[i]:
    #             if allowed[hat]:
    #                 allowed[hat] = False
    #                 c += f(allowed, i+1)
    #                 allowed[hat] = True
    #         cache[key] = c
    #         return c
    #     allowed = [True]*40
    #     return f(allowed, 0)
    def numberWays(self, hats: List[List[int]]) -> int:
        const = 10**9 + 7
        cache = {}
        matr = [[False] * 10 for i in range(40)]
        for j in range(len(hats)):
            for i in hats[j]:
                matr[i - 1][j] = True

        def s(mask_p, h, n):
            if n == 0:
                return 1
            if h < 0:
                return 0
            c = tuple(mask_p + [h])
            if c in cache:
                return cache[c]
            res = s(mask_p, h - 1, n)
            for p in range(len(matr[h])):
                if mask_p[p] and matr[h][p]:
                    mask_p[p] = False
                    res += s(mask_p, h - 1, n - 1)
                    mask_p[p] = True
            cache[c] = res
            return res
        mask_p = [True] * len(hats) + [False] * (10 - len(hats))
        return s(mask_p, 39, len(hats)) % const
