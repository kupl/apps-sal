# class Solution:
#     def numberWays(self, hats: List[List[int]]) -> int:
#         const = 10**9+7
#         cache = {}
#         matr = [[False]*len(hats) for i in range(40)]
#         maxx = -1
#         used_h = set()
#         for j in range(len(hats)):
#             for i in hats[j]:
#                 matr[i-1][j] = True
#                 maxx = max(i-1, maxx)
#                 used_h.add(i-1)
#         def s(mask_p, h, n):
#             if h < 0 or n > h+1:
#                 return 0
#             c = str(h)+mask_p
#             if c in cache:
#                 return cache[c]
#             res = s(mask_p, h-1, n)
#             if h in used_h:
#                 for p in range(len(matr[h])):
#                     if mask_p[p] == \"1\" and matr[h][p]:
#                         if n > 1:
#                             res += s(mask_p[:p] + \"0\" + mask_p[p+1:], h-1, n-1)
#                         else:
#                             res += 1
#             cache[c] = res%const
#             return res%const
#         mask_p = \"1\"*len(hats)
#         return s(mask_p, maxx, len(hats))%const
    
    
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        const = 10**9+7
        matr = [0 for i in range(40)]
        maxx = -1
        used_h = set()
        for j in range(len(hats)):
            for i in hats[j]:
                matr[i-1] += 2**(j)
                maxx = max(i-1, maxx)
                used_h.add(i-1)
        matr = matr[:maxx+1]
        mask_p = 2**len(hats)-1
        def s(mask_p, n, h, c_h, cache):
            if n > c_h:
                return 0
            if cache[mask_p][h] != None:
                return cache[mask_p][h]
            if mask_p == 0:
                return 1
            res = 0
            if h in used_h:
                c_h -= 1
                b = mask_p & matr[h]
                i = 0
                while b > 0:
                    if b & 1:
                        res += s(mask_p ^ (1 << i), n-1, h-1, c_h, cache)
                    b = b >> 1
                    i += 1
                # b = bin(mask_p & matr[h])
                # for p in range(2, len(b)):
                #     if b[p] == \"1\":
                #         res += s(mask_p ^ (1 << (len(b)-p-1)), n-1, h-1, c_h, cache)
            res += s(mask_p, n, h-1, c_h, cache)
            cache[mask_p][h] = res
            return cache[mask_p][h]
        return s(mask_p, len(hats), maxx, len(used_h), [[None]*(maxx+1) for i in range(mask_p+1)])%const
