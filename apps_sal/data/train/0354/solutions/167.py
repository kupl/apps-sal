class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        memo = [[[0 for k in range(16)] for j in range(7)] for i in range(n + 1)]
        result = 0
        mod = 10 ** 9 + 7

        def dfs(n, index, k):
            if n == 0:
                return 1
            if memo[n][index][k] != 0:
                return memo[n][index][k]
            result = 0
            for i in range(6):
                if i == index:
                    if rollMax[i] > k:
                        result += dfs(n - 1, i, k + 1)
                else:
                    result += dfs(n - 1, i, 1)
                    result %= mod
            memo[n][index][k] = result % mod
            return memo[n][index][k]

        for i in range(6):
            result += dfs(n - 1, i, 1)
            result %= mod
        return result % mod
