

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        const = 10**9 + 7
        matr = [0 for i in range(40)]
        maxx = -1
        used_h = set()
        for j in range(len(hats)):
            for i in hats[j]:
                matr[i - 1] += 2**(j)
                maxx = max(i - 1, maxx)
                used_h.add(i - 1)
        matr = matr[:maxx + 1]
        mask_p = 2**len(hats) - 1

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
                    if b % 2 == 0:
                        b /= 2
                    else:
                        b -= 1
                        b /= 2
                        res += s(mask_p - 2**(i), n - 1, h - 1, c_h, cache)
                    i += 1
            res += s(mask_p, n, h - 1, c_h, cache)
            cache[mask_p][h] = res % const
            return cache[mask_p][h]
        return s(mask_p, len(hats), maxx, len(used_h), [[None] * (maxx + 1) for i in range(mask_p + 1)])
