from functools import lru_cache


class Solution:

    def knightDialer(self, n: int) -> int:
        neighbors = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4]}

        @lru_cache(None)
        def dfs(i, n):
            if n == 1:
                return 1
            count = 0
            for x in neighbors[i]:
                count = (count + dfs(x, n - 1)) % (10 ** 9 + 7)
            return count
        ansr = 0
        for i in range(10):
            ansr = (ansr + dfs(i, n)) % (10 ** 9 + 7)
        return ansr
