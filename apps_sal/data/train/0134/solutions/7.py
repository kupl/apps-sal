class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        N = str(N)

        @lru_cache(None)
        def dfs(i, r, m):
            if i == len(N):
                return 1

            ans = 0
            limit = int(N[i]) if r else 9
            for k in range(0, limit + 1):
                if m & (1 << k) == 0:
                    mask = m | (1 << k) if m or k > 0 else 0
                    if k < limit or not r:
                        ans += dfs(i + 1, False, mask)
                    else:
                        ans += dfs(i + 1, True, mask)
            return ans

        return int(N) - dfs(0, True, 0) + 1
