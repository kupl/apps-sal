class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a = 1
        e = 1
        i = 1
        o = 1
        u = 1
        res = 0
        M = 1e9 + 7

        for x in range(n - 1):
            a1 = e
            e1 = (a + i) % M
            i1 = (a + e + u + o) % M
            o1 = (i + u) % M
            u1 = a
            a = a1
            e = e1
            i = i1
            o = o1
            u = u1

        res = int((a + e + i + o + u) % M)
        return res
