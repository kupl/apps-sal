class Solution:

    def countVowelPermutation(self, n: int) -> int:
        (a, e, i, o, u) = (1, 1, 1, 1, 1)
        p = 10 ** 9 + 7

        def next(a, e, i, o, u):
            (e, a, i, o, u) = ((a + i) % p, (e + i + u) % p, (e + o) % p, i % p, (i + o) % p)
            return (a, e, i, o, u)
        l = 1
        while l < n:
            (a, e, i, o, u) = next(a, e, i, o, u)
            l += 1
        return (a + e + i + o + u) % p
