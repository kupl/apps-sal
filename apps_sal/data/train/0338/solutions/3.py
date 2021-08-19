class Solution:

    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:

        @lru_cache(None)
        def dfs(k, j, b1, b2):
            if k == n:
                return 1
            start = ord(s1[k]) if b1 else ord('a')
            end = ord(s2[k]) if b2 else ord('z')
            res = 0
            for x in range(start, end + 1):
                c = chr(x)
                l = j
                while l > 0 and c != evil[l]:
                    l = lps[l - 1]
                nevil = True
                if c == evil[l]:
                    l += 1
                    if l == m:
                        nevil = False
                if nevil:
                    res += dfs(k + 1, l, b1 and c == s1[k], b2 and c == s2[k])
                    res %= mod
            return res
        m = len(evil)
        lps = [0] * m
        for i in range(1, m):
            j = lps[i - 1]
            while j > 0 and evil[j] != evil[i]:
                j = lps[j - 1]
            if evil[j] == evil[i]:
                lps[i] = j + 1
        mod = 10 ** 9 + 7
        return dfs(0, 0, True, True)
