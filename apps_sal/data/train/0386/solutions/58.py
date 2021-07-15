class Solution:
    def countVowelPermutation(self, n: int) -> int:
        '''       
        # TLE top-down
        graph = {'a': ['e'], 'e':['a', 'i'],\\
                'i': ['a','e','o','u'], 'o': ['i', 'u'],\\
                'u': ['a']}
        mod = 10**9+7
        @functools.lru_cache(None)
        def dp(c, i):
            if i == 1:
                return 1
            return sum(dp(key, i-1) for key in graph[c])%mod
        return sum(dp(key, n) for key in graph)%mod
        '''
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(1, n):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
        return (a + e + i + o + u) % (10**9 + 7)
