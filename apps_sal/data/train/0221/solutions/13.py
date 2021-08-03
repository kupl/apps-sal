class Solution:
    def longestDupSubstring(self, S: str) -> str:

        def rk(m):

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
                #y = (y-num[i-1]*p)*b+num[i-1+m]

                if y not in mp:
                    mp[y] = i
                else:
                    return i

            return n

        n = len(S)

        b = 26                      # no need to be 128

        # mod = 10**9+7              # too small => conflict
        mod = 2**32                 # here

        num = []
        for i in range(n):
            num.append(ord(S[i]) - ord('a'))

        l = 1
        r = n

        while l < r:

            m = (l + r) // 2

            if rk(m) == n:
                r = m
            else:
                l = m + 1

        x = l - 1

        if x == 0:
            return ''

        k = rk(x)

        return S[k:k + x]
