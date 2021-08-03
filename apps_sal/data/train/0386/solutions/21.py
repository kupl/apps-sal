class Solution:
    def countVowelPermutation(self, n: int) -> int:

        graph = {'a': ['e'], 'e': ['a', 'i'], 'i': ['a', 'e', 'o', 'u'], 'o': ['i', 'u'], 'u': ['a']}
        dp = [[None for j in range(5)] for i in range(n + 1)]
        get = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        mod = int(10**9) + 7

        def dfs(n, node):
            if n == 1:
                return 1
            elif dp[n][get[node]]:
                return dp[n][get[node]]
            else:
                ans = 0
                for w in graph[node]:
                    ans += dfs(n - 1, w) % mod
                dp[n][get[node]] = ans
                return ans

        x = 0
        for b in 'aeiou':
            x += dfs(n, b) % mod
        return x % mod
