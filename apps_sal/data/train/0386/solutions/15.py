class Solution:

    def countVowelPermutation(self, n: int) -> int:

        @lru_cache(None)
        def dfs(i, j):
            if i == 1:
                return 1
            if j == 'a':
                return dfs(i - 1, 'e') + dfs(i - 1, 'i') + dfs(i - 1, 'u')
            elif j == 'e':
                return dfs(i - 1, 'a') + dfs(i - 1, 'i')
            elif j == 'i':
                return dfs(i - 1, 'e') + dfs(i - 1, 'o')
            elif j == 'o':
                return dfs(i - 1, 'i')
            return dfs(i - 1, 'i') + dfs(i - 1, 'o')
        return sum((dfs(n, i) for i in ('a', 'e', 'i', 'o', 'u'))) % (10 ** 9 + 7)
