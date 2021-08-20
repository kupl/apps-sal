class Solution:

    def knightDialer(self, n: int) -> int:
        path = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        M = 10 ** 9 + 7

        @lru_cache
        def paths(i, n):
            if n == 1:
                return len(path[i])
            if n == 0:
                return 1
            s = 0
            for v in path[i]:
                s += paths(v, n - 1)
            return s % M
        ans = 0
        for k in path:
            ans += paths(k, n - 1)
        return ans % M
