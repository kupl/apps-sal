MOD = 10**9 + 7


class Solution:
    def knightDialer(self, n: int) -> int:
        @lru_cache(None)
        def dfs(i, j, k):
            # base case
            if k == n - 1:
                return 1
            # recursion
            res = 0
            for di, dj in [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]:
                ni, nj = i + di, j + dj
                if not (0 <= ni < 4 and 0 <= nj < 3):
                    continue
                if (ni, nj) in [(3, 0), (3, 2)]:
                    continue
                res += dfs(ni, nj, k + 1)
                res %= MOD
            return res

        ans = 0
        for i, j in product(range(4), range(3)):
            if (i, j) in [(3, 0), (3, 2)]:
                continue
            ans += dfs(i, j, 0)
        return ans % MOD
