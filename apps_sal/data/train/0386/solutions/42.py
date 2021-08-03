class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a = e = i = o = u = 1
        for p in range(n - 1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
        return (a + e + i + o + u) % (10**9 + 7)
