class Solution:

    def countVowelPermutation(self, n: int) -> int:
        m = 10 ** 9 + 7
        a = e = i = o = u = 1
        for _ in range(n - 1):
            (a, e, i, o, u) = ((e + i + u) % m, (a + i) % m, (e + o) % m, i % m, (i + o) % m)
        return (a + e + i + o + u) % m
