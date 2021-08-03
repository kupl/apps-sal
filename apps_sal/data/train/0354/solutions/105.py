from functools import lru_cache


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def dfs(n, last_idx, curr_len):
            if n == 0:
                return 1

            cnt = 0
            for i in range(6):
                if i != last_idx or curr_len < rollMax[i]:
                    temp = 1 if i != last_idx else curr_len + 1
                    cnt += dfs(n - 1, i, temp)
            return cnt % mod
        return dfs(n, -1, 0)
