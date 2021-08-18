class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        for k in range(1, n):
            a, e, i, o, u = i + e + u, a + i, e + o, i, i + o
        return (a + e + i + o + u) % (10**9 + 7)
