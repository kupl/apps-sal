class Solution:

    def numWays(self, s: str) -> int:
        n = s.count('1')
        if n % 3 != 0:
            return 0
        if n == 0:
            return (len(s) - 1) * (len(s) - 2) // 2 % (10 ** 9 + 7)
        m = n // 3
        L = s.split('1')
        return (len(L[m]) + 1) * (len(L[2 * m]) + 1) % (10 ** 9 + 7)
