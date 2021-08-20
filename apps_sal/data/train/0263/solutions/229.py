class Solution:

    def knightDialer(self, n: int) -> int:
        mm = {1: [6, 8], 2: [7, 9], 3: [8, 4], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [6, 4]}
        ans = 0

        @lru_cache(maxsize=None)
        def dfs(val, rem):
            if rem == 0:
                return 1
            res = 0
            for adj in mm[val]:
                res += dfs(adj, rem - 1)
            return res
        for key in list(mm.keys()):
            ans += dfs(key, n - 1)
        return ans % 1000000007
