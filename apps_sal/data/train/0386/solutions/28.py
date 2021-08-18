class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = (10**9 + 7)

        @lru_cache
        def dfs(p, n):
            if n == 0:
                return 1

            if p == 'a':
                return dfs('e', n - 1)
            if p == 'e':
                return sum([dfs(c, n - 1) for c in ['a', 'i']])
            if p == 'i':
                return sum([dfs(c, n - 1) for c in ['a', 'e', 'o', 'u']])
            elif p == 'o':
                return sum([dfs(c, n - 1) for c in ['i', 'u']])
            else:
                return dfs('a', n - 1)

        return sum([dfs(c, n - 1) for c in ['a', 'e', 'i', 'o', 'u']]) % mod
