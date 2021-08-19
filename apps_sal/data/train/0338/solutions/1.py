class Solution:

    def findGoodStrings(self, N, *args):
        from functools import lru_cache
        (s1, s2, evil) = [list(map(ord, i)) for i in args]
        mod = 10 ** 9 + 7

        def kmp(l, c):
            while l and evil[l] != c:
                l = f[l - 1]
            if evil[l] == c:
                l += 1
            return l
        f = [0] * len(evil)
        for i in range(1, len(evil)):
            f[i] = kmp(f[i - 1], evil[i])

        @lru_cache(None)
        def dp(i=0, lcp=0, f1=False, f2=False):
            if lcp == len(evil):
                return 0
            if i == N:
                return 1
            ans = 0
            for char in range(f1 and 97 or s1[i], f2 and 123 or s2[i] + 1):
                ans += dp(i + 1, kmp(lcp, char), f1 or char > s1[i], f2 or char < s2[i])
                ans %= mod
            return ans
        return dp()
