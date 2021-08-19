class Solution:

    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        nstrs = [1] * 5
        while n > 1:
            (a, e, i, o, u) = nstrs
            nstrs[0] = e
            nstrs[1] = a + i
            nstrs[2] = a + e + o + u
            nstrs[3] = i + u
            nstrs[4] = a
            n -= 1
        return sum(nstrs) % mod
