class Solution:

    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        mem = {}

        def dfs(p, n):
            if (p, n) in mem:
                return mem[p, n]
            if n == 0:
                return 1
            res = 0
            if p == 'a':
                res = dfs('e', n - 1)
            elif p == 'e':
                res = sum([dfs(c, n - 1) for c in ['a', 'i']])
            elif p == 'i':
                res = sum([dfs(c, n - 1) for c in ['a', 'e', 'o', 'u']])
            elif p == 'o':
                res = sum([dfs(c, n - 1) for c in ['i', 'u']])
            else:
                res = dfs('a', n - 1)
            mem[p, n] = res % mod
            return res % mod
        return sum([dfs(c, n - 1) for c in ['a', 'e', 'i', 'o', 'u']]) % mod
