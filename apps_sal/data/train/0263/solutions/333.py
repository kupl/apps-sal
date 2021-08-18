class Solution:
    d = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]

    def dfs(self, i, n, cache={}):
        if n == 0:
            return 1
        if (i, n) not in cache:
            cache[i, n] = sum(self.dfs(val, n - 1) for val in self.d[i])
        return cache[i, n]

    def knightDialer(self, n: int) -> int:
        mod = int(1e9) + 7
        return sum(self.dfs(i, n - 1) for i in range(10)) % mod
