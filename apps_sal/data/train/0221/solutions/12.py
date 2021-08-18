class Solution:
    def longestDupSubstring(self, S: str) -> str:

        def rk(m):

            nonlocal idx
            mp = {}
            p = b**(m - 1)
            p %= mod

            y = 0
            for i in range(m):
                y = y * b + num[i]
            y %= mod

            mp[y] = 0

            for i in range(1, n - m + 1):
                y = ((y - num[i - 1] * p % mod) * b % mod + num[i - 1 + m]) % mod

                if y in mp:
                    idx = i
                    return 0
                else:
                    mp[y] = i

            return 1

        n = len(S)
        b = 26
        mod = 2**32

        z = ord('a')
        num = [ord(S[i]) - z for i in range(n)]

        l = 1
        r = n
        idx = 0
        while l < r:

            m = (l + r) // 2

            if rk(m) > 0:
                r = m
            else:
                l = m + 1

        return S[idx:idx + l - 1]
