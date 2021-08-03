class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7

        @lru_cache(None)
        def go(ch, n):
            if n == 0:
                return 1
            if (ch == 'a'):
                return go('e', n - 1)
            elif (ch == 'e'):
                return go('a', n - 1) + go('i', n - 1)
            elif (ch == 'i'):
                return go('a', n - 1) + go('e', n - 1) + go('o', n - 1) + go('u', n - 1)
            elif (ch == 'o'):
                return go('i', n - 1) + go('u', n - 1)
            else:
                return go('a', n - 1)

        res1 = go('a', n - 1) % mod
        res2 = go('e', n - 1) % mod
        res3 = go('i', n - 1) % mod
        res4 = go('o', n - 1) % mod
        res5 = go('u', n - 1) % mod

        return (res1 + res2 + res3 + res4 + res5) % mod
