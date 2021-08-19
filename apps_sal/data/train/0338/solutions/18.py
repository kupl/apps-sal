import functools


class Solution:

    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:

        def calc(k, char):
            i = 0
            while i <= k and (not evil[i:k] + char == evil[:k - i + 1]):
                i += 1
            return k - i + 1

        @functools.lru_cache(None)
        def dp(i, k, limit_low, limit_high):
            if k == len(evil):
                return 0
            if i == n:
                return 1
            ans = 0
            min_char = s1[i] if limit_low else 'a'
            max_char = s2[i] if limit_high else 'z'
            for o in range(ord(min_char), ord(max_char) + 1):
                curr = chr(o)
                if curr == evil[k]:
                    ans += dp(i + 1, k + 1, limit_low and curr == min_char, limit_high and curr == max_char)
                else:
                    ans += dp(i + 1, calc(k, curr), limit_low and curr == min_char, limit_high and curr == max_char)
            return ans % (10 ** 9 + 7)
        return dp(0, 0, True, True) % (10 ** 9 + 7)
