class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        kMod = 1e9+7
        for k in range(2, n+1):
            aa = (e + i + u) % kMod
            ee = (a + i) % kMod
            ii = (e + o) % kMod
            oo = i % kMod
            uu = (i + o) % kMod
            a = aa
            e = ee
            i = ii
            o = oo
            u = uu
        return int((a + e + i + o + u) % kMod)
