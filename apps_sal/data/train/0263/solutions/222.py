class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7
        nei = {0: [4, 6,], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        
        @lru_cache(None)
        def dfs(i, pre):
            if i == n:
                return 1
            cand = nei[pre] if pre != None else range(10)
            ans = 0
            for k in cand:
                ans += dfs(i + 1, k) % mod
            return ans % mod
        
        return dfs(0, None)
