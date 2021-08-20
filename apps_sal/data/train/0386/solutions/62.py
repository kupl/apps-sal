class Solution:

    def countVowelPermutation(self, n: int) -> int:
        a = 1
        e = 1
        i = 1
        o = 1
        u = 1
        kmod = pow(10, 9) + 7
        for k in range(2, n + 1):
            aa = (e + i + u) % kmod
            ee = (a + i) % kmod
            ii = (e + o) % kmod
            oo = i % kmod
            uu = (i + o) % kmod
            a = aa
            e = ee
            i = ii
            o = oo
            u = uu
        return sum([a, e, i, o, u]) % kmod
