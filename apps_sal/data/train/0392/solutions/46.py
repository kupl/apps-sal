class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = sum(1 for c in s if c == '1')
        if n % 3 != 0:
            return 0
        if n == 0:
            t = (len(s) - 1) * (len(s) - 2) // 2
            return t % MOD
        n //= 3

        def f(s, n):
            i = 0
            while n:
                n -= 1 if s[i] == '1' else 0
                i += 1
            k = 1
            while s[i] == '0':
                k += 1
                i += 1
            return k

        return f(s, n) * f(''.join(reversed(s)), n) % MOD
