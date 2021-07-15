class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def dfs(i, num, k):
            if i == n:
                return 1
            ans = 0
            for j in range(6):
                if j != num:
                    ans += dfs(i + 1, j, 1)
                elif k < rollMax[j]:
                    ans += dfs(i + 1, j, k + 1)
            return ans

        ans = 0
        for i in range(6):
            ans += dfs(1, i, 1)
        return ans % mod
                    

