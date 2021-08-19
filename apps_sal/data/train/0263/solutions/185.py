class Solution:

    def knightDialer(self, n: int) -> int:
        d = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}

        @lru_cache(None)
        def dfs(i, n):
            if n == 1:
                return 1
            else:
                res = 0
                for c in d[i]:
                    res += dfs(c, n - 1)
                return res % (10 ** 9 + 7)
        return sum((dfs(i, n) for i in range(10))) % (10 ** 9 + 7)
