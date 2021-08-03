class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        N = len(hats)
        for i, h in enumerate(hats):
            hats[i] = set(h)
        mod = (10 ** 9) + 7

        @lru_cache(None)
        def rec(cur, mask):
            if cur > 41:
                return 0
            if mask == 0:
                return 1

            ans = 0
            for i in range(N):
                if (mask & (1 << i)) == 0:
                    continue
                if cur not in hats[i]:
                    continue
                ans += rec(cur + 1, mask ^ (1 << i))
            ans += rec(cur + 1, mask)

            return ans

        return rec(0, (2**N) - 1) % mod
