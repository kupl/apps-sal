class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n == 1:
            return 5
        a, e, o, u, i = 1, 1, 1, 1, 1
        for _ in range(1, n):
            a, e, o, u, i = e + u + i, i + a, i, i + o, e + o
        return (a + e + o + u + i) % (10**9 + 7)
