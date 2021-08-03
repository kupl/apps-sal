class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dfs(n, prev, consecutive):
            if n == 0:
                return 1

            res = 0

            for next_num in range(1, 7):
                if next_num == prev:
                    if consecutive < rollMax[next_num - 1]:
                        res += dfs(n - 1, prev, consecutive + 1)
                else:
                    res += dfs(n - 1, next_num, 1)

            return res

        return dfs(n, None, 0) % MOD
