from enum import IntEnum


class Solution:
    (found, not_found) = (0, 0)

    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7

        class Vowel(IntEnum):
            A = 0
            E = 1
            I = 2
            O = 3
            U = 4
        nstrs = [1] * 5
        while n > 1:
            (a, e, i, o, u) = nstrs
            nstrs[Vowel.A] = e
            nstrs[Vowel.E] = a + i
            nstrs[Vowel.I] = a + e + o + u
            nstrs[Vowel.O] = i + u
            nstrs[Vowel.U] = a
            n -= 1
        return sum(nstrs) % mod
